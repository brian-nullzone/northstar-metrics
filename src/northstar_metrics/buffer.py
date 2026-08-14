from __future__ import annotations


class EventBuffer:
    def __init__(self) -> None:
        self._items: list[dict] = []

    def add(self, item: dict) -> None:
        self._items.append(item)

    def snapshot(self) -> list[dict]:
        return list(self._items)

    def clear(self) -> int:
        n = len(self._items)
        self._items.clear()
        return n

    def __len__(self) -> int:
        return len(self._items)
