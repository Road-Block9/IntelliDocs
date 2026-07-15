class PDFExtractionError(Exception):
    """Base class for controlled raw PDF extraction failures."""


class PDFNotFoundError(PDFExtractionError):
    """Raised when the requested source file does not exist."""


class UnsupportedFileTypeError(PDFExtractionError):
    """Raised when the requested source does not have a PDF extension."""


class UnreadablePDFError(PDFExtractionError):
    """Raised when PyMuPDF cannot open or read the source PDF."""


class EmptyPDFError(PDFExtractionError):
    """Raised when a valid PDF contains no pages."""
