from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import fitz

from app.services.extraction.errors import (
    EmptyPDFError,
    PDFNotFoundError,
    UnreadablePDFError,
    UnsupportedFileTypeError,
)
from app.services.extraction.ocr import (
    OCRAvailability,
    check_ocr_availability,
    page_may_need_ocr,
)

SCHEMA_VERSION = "1.0"
_ITALIC_FLAG = 1 << 1
_BOLD_FLAG = 1 << 4


def extract_pdf(source_path: str | Path, *, enable_ocr: bool = False) -> dict[str, Any]:
    """Extract layout-preserving raw evidence without interpreting document structure."""
    pdf_path = _validate_source_path(source_path)
    ocr_availability = check_ocr_availability()

    try:
        document = fitz.open(pdf_path)
    except (fitz.FileDataError, RuntimeError, ValueError, OSError) as exc:
        raise UnreadablePDFError(f"Unable to open PDF '{pdf_path.name}': {exc}") from exc

    try:
        if document.needs_pass:
            raise UnreadablePDFError(
                f"Unable to read PDF '{pdf_path.name}': the file is encrypted or password protected."
            )
        if document.page_count == 0:
            raise EmptyPDFError(f"PDF '{pdf_path.name}' contains no pages.")

        pages = [
            _extract_page(
                document.load_page(page_index),
                pdf_filename=pdf_path.name,
                page_number=page_index + 1,
                enable_ocr=enable_ocr,
                ocr_availability=ocr_availability,
            )
            for page_index in range(document.page_count)
        ]
    except (EmptyPDFError, UnreadablePDFError):
        raise
    except (fitz.FileDataError, RuntimeError, ValueError, OSError) as exc:
        raise UnreadablePDFError(f"Unable to extract PDF '{pdf_path.name}': {exc}") from exc
    finally:
        document.close()

    return {
        "schema_version": SCHEMA_VERSION,
        "pdf_filename": pdf_path.name,
        "page_count": len(pages),
        "ocr_requested": enable_ocr,
        "ocr_tooling": ocr_availability.to_dict(),
        "pages": pages,
    }


def write_extraction_json(
    extraction: dict[str, Any],
    output_directory: str | Path,
) -> Path:
    """Write an extraction record to the generated-output directory supplied by the caller."""
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_name = f"{Path(extraction['pdf_filename']).stem}.raw.json"
    output_path = output_dir / output_name
    output_path.write_text(
        json.dumps(extraction, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


def _validate_source_path(source_path: str | Path) -> Path:
    pdf_path = Path(source_path)
    if not pdf_path.exists():
        raise PDFNotFoundError(f"PDF file not found: {pdf_path}")
    if not pdf_path.is_file():
        raise PDFNotFoundError(f"PDF path is not a file: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise UnsupportedFileTypeError(f"Expected a .pdf file, received: {pdf_path.name}")
    return pdf_path


def _extract_page(
    page: fitz.Page,
    *,
    pdf_filename: str,
    page_number: int,
    enable_ocr: bool,
    ocr_availability: OCRAvailability,
) -> dict[str, Any]:
    image_count = len(page.get_image_info(xrefs=True))
    embedded_text = page.get_text("text")
    selectable_text_present = bool(embedded_text.strip())
    ocr_may_be_needed = page_may_need_ocr(
        selectable_text_present=selectable_text_present,
        image_count=image_count,
    )

    text_dictionary = page.get_text("dict", sort=False)
    extraction_method = "embedded_text"
    ocr_attempted = False
    ocr_succeeded = False
    ocr_error: str | None = None

    if enable_ocr and ocr_may_be_needed:
        if not ocr_availability.available:
            ocr_error = ocr_availability.detail
        else:
            ocr_attempted = True
            try:
                text_page = page.get_textpage_ocr(language="eng", dpi=300, full=True)
                text_dictionary = page.get_text("dict", textpage=text_page, sort=False)
                extraction_method = "ocr"
                ocr_succeeded = True
            except (RuntimeError, ValueError, OSError) as exc:
                ocr_error = f"Tesseract OCR failed for page {page_number}: {exc}"

    blocks = _extract_text_blocks(
        text_dictionary,
        pdf_filename=pdf_filename,
        page_number=page_number,
        extraction_method=extraction_method,
    )
    return {
        "pdf_filename": pdf_filename,
        "page_number": page_number,
        "width": float(page.rect.width),
        "height": float(page.rect.height),
        "text_block_count": len(blocks),
        "image_count": image_count,
        "selectable_text_present": selectable_text_present,
        "ocr_may_be_needed": ocr_may_be_needed,
        "ocr_attempted": ocr_attempted,
        "ocr_succeeded": ocr_succeeded,
        "ocr_error": ocr_error,
        "blocks": blocks,
    }


def _extract_text_blocks(
    text_dictionary: dict[str, Any],
    *,
    pdf_filename: str,
    page_number: int,
    extraction_method: str,
) -> list[dict[str, Any]]:
    text_blocks = [block for block in text_dictionary.get("blocks", []) if block.get("type") == 0]
    return [
        _build_block(
            block,
            pdf_filename=pdf_filename,
            page_number=page_number,
            reading_order_index=index,
            extraction_method=extraction_method,
        )
        for index, block in enumerate(text_blocks)
    ]


def _build_block(
    block: dict[str, Any],
    *,
    pdf_filename: str,
    page_number: int,
    reading_order_index: int,
    extraction_method: str,
) -> dict[str, Any]:
    lines = block.get("lines", [])
    spans = [span for line in lines for span in line.get("spans", [])]
    line_texts = ["".join(str(span.get("text", "")) for span in line.get("spans", [])) for line in lines]
    meaningful_spans = [span for span in spans if str(span.get("text", "")).strip()]
    dominant_span = _dominant_span(meaningful_spans)

    span_evidence = [_span_evidence(span) for span in spans]
    block_bold = _consistent_indicator(span_evidence, "bold")
    block_italic = _consistent_indicator(span_evidence, "italic")

    return {
        "pdf_filename": pdf_filename,
        "page_number": page_number,
        "reading_order_index": reading_order_index,
        "raw_text": "\n".join(line_texts),
        "bounding_box": _bbox(block.get("bbox")),
        "font_size": float(dominant_span["size"]) if dominant_span and dominant_span.get("size") is not None else None,
        "font_name": str(dominant_span["font"]) if dominant_span and dominant_span.get("font") else None,
        "font_style": _font_style(block_bold, block_italic),
        "bold": block_bold,
        "italic": block_italic,
        "extraction_method": extraction_method,
        "spans": span_evidence,
    }


def _span_evidence(span: dict[str, Any]) -> dict[str, Any]:
    flags = int(span.get("flags", 0))
    font_name = str(span.get("font", ""))
    normalized_font_name = font_name.casefold()
    bold = bool(flags & _BOLD_FLAG) or "bold" in normalized_font_name
    italic = bool(flags & _ITALIC_FLAG) or any(
        marker in normalized_font_name for marker in ("italic", "oblique")
    )
    return {
        "raw_text": str(span.get("text", "")),
        "bounding_box": _bbox(span.get("bbox")),
        "font_size": float(span["size"]) if span.get("size") is not None else None,
        "font_name": font_name or None,
        "bold": bold,
        "italic": italic,
    }


def _dominant_span(spans: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not spans:
        return None
    keys = [(span.get("font"), span.get("size"), int(span.get("flags", 0))) for span in spans]
    weights: Counter[tuple[Any, Any, int]] = Counter()
    for key, span in zip(keys, spans, strict=True):
        weights[key] += max(len(str(span.get("text", "")).strip()), 1)
    dominant_key = weights.most_common(1)[0][0]
    return next(span for key, span in zip(keys, spans, strict=True) if key == dominant_key)


def _consistent_indicator(spans: list[dict[str, Any]], field: str) -> bool | None:
    values = {bool(span[field]) for span in spans if str(span["raw_text"]).strip()}
    if len(values) != 1:
        return None
    return values.pop()


def _font_style(bold: bool | None, italic: bool | None) -> str | None:
    if bold is None or italic is None:
        return None
    if bold and italic:
        return "bold_italic"
    if bold:
        return "bold"
    if italic:
        return "italic"
    return "regular"


def _bbox(value: Any) -> list[float] | None:
    if value is None or len(value) != 4:
        return None
    return [float(coordinate) for coordinate in value]
