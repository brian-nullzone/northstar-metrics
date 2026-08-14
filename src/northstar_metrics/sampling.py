from __future__ import annotations


def keep(n: int, every: int) -> bool:
    if every <= 1:
        return True
    return n % every == 0
