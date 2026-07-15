from __future__ import annotations

import shutil
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class OCRAvailability:
    available: bool
    engine: str
    detail: str

    def to_dict(self) -> dict[str, bool | str]:
        return asdict(self)


def check_ocr_availability() -> OCRAvailability:
    """Report whether optional Tesseract OCR is discoverable on PATH."""
    executable = shutil.which("tesseract")
    if executable is None:
        return OCRAvailability(
            available=False,
            engine="tesseract",
            detail=(
                "Tesseract was not found on PATH. Embedded-text extraction "
                "remains available; OCR-requested pages will be left unprocessed."
            ),
        )

    return OCRAvailability(
        available=True,
        engine="tesseract",
        detail=f"Tesseract executable found at {executable}.",
    )


def page_may_need_ocr(*, selectable_text_present: bool, image_count: int) -> bool:
    """Flag likely scanned pages without treating intentionally blank pages as scans."""
    return not selectable_text_present and image_count > 0
