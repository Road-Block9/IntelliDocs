from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from app.services.extraction.errors import PDFExtractionError
from app.services.extraction.pdf_extractor import extract_pdf, write_extraction_json

DEFAULT_OUTPUT_DIRECTORY = Path("generated-output/raw-extraction")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract layout-preserving raw blocks from a PDF into JSON."
    )
    parser.add_argument("pdf_path", type=Path, help="Path to the source PDF.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIRECTORY,
        help=f"Generated JSON directory (default: {DEFAULT_OUTPUT_DIRECTORY}).",
    )
    parser.add_argument(
        "--enable-ocr",
        action="store_true",
        help="Attempt Tesseract only on image-bearing pages without selectable text.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        extraction = extract_pdf(args.pdf_path, enable_ocr=args.enable_ocr)
        output_path = write_extraction_json(extraction, args.output_dir)
    except PDFExtractionError as exc:
        print(f"Extraction failed: {exc}", file=sys.stderr)
        return 2

    ocr_pages = [
        str(page["page_number"])
        for page in extraction["pages"]
        if page["ocr_may_be_needed"]
    ]
    print(f"Wrote: {output_path}")
    print(f"Pages: {extraction['page_count']}")
    print(f"OCR tooling: {extraction['ocr_tooling']['detail']}")
    print(f"Pages that may need OCR: {', '.join(ocr_pages) if ocr_pages else 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
