from __future__ import annotations


def chunks(items: list[dict], size: int) -> list[list[dict]]:
    if size < 1:
        size = 1
    return [items[i : i + size] for i in range(0, len(items), size)]
