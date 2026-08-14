"""Optional collector reachability check before a worker starts emitting."""

from __future__ import annotations

import urllib.error
import urllib.request


def _default_probe() -> str:
    return "http://127.0.0.1:9090/health"


def collector_up(url: str | None = None) -> bool:
    target = url or _default_probe()
    req = urllib.request.Request(
        target,
        headers={"User-Agent": "northstar-metrics/0.1.1"},
    )
    try:
        with urllib.request.urlopen(req, timeout=0.3) as resp:
            resp.read(64)
        return True
    except (OSError, urllib.error.URLError):
        return False

