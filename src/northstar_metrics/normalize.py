"""Tag key normalization."""

from __future__ import annotations

import re

_SAFE = re.compile(r"^[a-z0-9_.]+$")


def normalize_key(key: str) -> str:
    out = key.strip().lower().replace(" ", "_")
    if not _SAFE.match(out):
        raise ValueError(f"unsafe metric key: {key!r}")
    return out
