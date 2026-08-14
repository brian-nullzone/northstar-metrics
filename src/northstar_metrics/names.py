from __future__ import annotations

from .normalize import normalize_key


def event_name(parts: list[str]) -> str:
    return ".".join(normalize_key(p) for p in parts if p.strip())
