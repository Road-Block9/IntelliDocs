from __future__ import annotations

import json
from pathlib import Path

import fitz
import pytest

from app.services.extraction import pdf_extractor
from app.services.extraction.errors import (
    EmptyPDFError,
    PDFNotFoundError,
    UnreadablePDFError,
    UnsupportedFileTypeError,
)
from app.services.extraction.pdf_extractor import extract_pdf, write_extraction_json
from app.services.extraction.ocr import OCRAvailability


def _make_text_pdf(path: Path) -> None:
    document = fitz.open()
    page = document.new_page(width=300, height=400)
    page.insert_text((40, 60), "Synthetic PDF text", fontsize=12, fontname="helv")
    document.save(path)
    document.close()


def _make_image_only_pdf(path: Path) -> None:
    image_document = fitz.open()
    image_page = image_document.new_page(width=20, height=20)
    pixmap = image_page.get_pixmap()
    image_bytes = pixmap.tobytes("png")
    image_document.close()

    document = fitz.open()
    page = document.new_page(width=300, height=400)
    page.insert_image(fitz.Rect(20, 20, 280, 380), stream=image_bytes)
    document.save(path)
    document.close()


def test_extracts_layout_and_font_evidence_from_embedded_text(tmp_path: Path) -> None:
    pdf_path = tmp_path / "sample.pdf"
    _make_text_pdf(pdf_path)

    result = extract_pdf(pdf_path)

    assert result["pdf_filename"] == "sample.pdf"
    assert result["page_count"] == 1
    page = result["pages"][0]
    assert page["width"] == pytest.approx(300)
    assert page["height"] == pytest.approx(400)
    assert page["selectable_text_present"] is True
    assert page["ocr_may_be_needed"] is False
    assert page["text_block_count"] == 1
    block = page["blocks"][0]
    assert block["reading_order_index"] == 0
    assert block["raw_text"] == "Synthetic PDF text"
    assert block["font_size"] == pytest.approx(12)
    assert block["font_name"] == "Helvetica"
    assert block["extraction_method"] == "embedded_text"
    assert len(block["bounding_box"]) == 4
    assert block["spans"][0]["raw_text"] == "Synthetic PDF text"


def test_flags_image_only_page_as_possible_ocr_candidate(tmp_path: Path) -> None:
    pdf_path = tmp_path / "scan.pdf"
    _make_image_only_pdf(pdf_path)

    result = extract_pdf(pdf_path)

    page = result["pages"][0]
    assert page["image_count"] == 1
    assert page["selectable_text_present"] is False
    assert page["ocr_may_be_needed"] is True
    assert page["ocr_attempted"] is False


def test_unavailable_ocr_is_reported_without_breaking_extraction(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pdf_path = tmp_path / "scan.pdf"
    _make_image_only_pdf(pdf_path)
    unavailable = OCRAvailability(
        available=False,
        engine="tesseract",
        detail="Tesseract is unavailable for this test.",
    )
    monkeypatch.setattr(pdf_extractor, "check_ocr_availability", lambda: unavailable)

    result = extract_pdf(pdf_path, enable_ocr=True)

    page = result["pages"][0]
    assert result["ocr_tooling"] == unavailable.to_dict()
    assert page["ocr_may_be_needed"] is True
    assert page["ocr_attempted"] is False
    assert page["ocr_succeeded"] is False
    assert page["ocr_error"] == unavailable.detail
    assert page["blocks"] == []


def test_writes_generated_json(tmp_path: Path) -> None:
    pdf_path = tmp_path / "sample.pdf"
    _make_text_pdf(pdf_path)
    extraction = extract_pdf(pdf_path)

    output_path = write_extraction_json(extraction, tmp_path / "generated")

    assert output_path.name == "sample.raw.json"
    assert json.loads(output_path.read_text(encoding="utf-8")) == extraction


def test_missing_file_has_controlled_error(tmp_path: Path) -> None:
    with pytest.raises(PDFNotFoundError, match="not found"):
        extract_pdf(tmp_path / "missing.pdf")


def test_non_pdf_file_has_controlled_error(tmp_path: Path) -> None:
    text_path = tmp_path / "notes.txt"
    text_path.write_text("not a PDF", encoding="utf-8")

    with pytest.raises(UnsupportedFileTypeError, match="Expected a .pdf"):
        extract_pdf(text_path)


def test_corrupt_pdf_has_controlled_error(tmp_path: Path) -> None:
    corrupt_path = tmp_path / "corrupt.pdf"
    corrupt_path.write_bytes(b"%PDF-1.7\nnot a readable PDF")

    with pytest.raises(UnreadablePDFError, match="Unable to open PDF"):
        extract_pdf(corrupt_path)


def test_empty_pdf_has_controlled_error(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    source = tmp_path / "empty.pdf"
    source.write_bytes(b"%PDF-mocked")

    class EmptyDocument:
        needs_pass = False
        page_count = 0

        def close(self) -> None:
            return None

    monkeypatch.setattr(pdf_extractor.fitz, "open", lambda _: EmptyDocument())

    with pytest.raises(EmptyPDFError, match="contains no pages"):
        extract_pdf(source)
