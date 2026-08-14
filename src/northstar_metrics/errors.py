class MetricsError(Exception):
    """Base error for the client."""


class FlushError(MetricsError):
    """Raised only when the caller opts into strict flush."""
