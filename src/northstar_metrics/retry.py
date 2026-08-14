from __future__ import annotations


def next_delay(attempt: int, base_s: float = 0.25, cap_s: float = 4.0) -> float:
    if attempt < 1:
        return base_s
    delay = base_s * (2 ** (attempt - 1))
    return cap_s if delay > cap_s else delay
