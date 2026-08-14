from __future__ import annotations

import json


def encode_events(events: list[dict]) -> bytes:
    return json.dumps({"events": events}, separators=(",", ":")).encode()
