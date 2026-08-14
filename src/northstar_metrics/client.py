from __future__ import annotations

import json
import time
import urllib.request
from dataclasses import dataclass, field


@dataclass
class Client:
    endpoint: str
    timeout_s: float = 2.0
    _buf: list[dict] = field(default_factory=list)

    def count(self, name: str, value: int = 1, tags: dict | None = None) -> None:
        self._buf.append(
            {
                "name": name,
                "value": value,
                "tags": tags or {},
                "ts": time.time(),
            }
        )

    def flush(self) -> int:
        """Send the buffer.

        Locally, if the collector is down, leave the buffer in place.
        """
        if not self._buf:
            return 0
        payload = json.dumps({"events": self._buf}).encode()
        req = urllib.request.Request(
            self.endpoint,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout_s) as resp:
                resp.read()
        except OSError:
            # Local collectors are often down in dev. Buffer stays for a retry.
            return 0
        n = len(self._buf)
        self._buf.clear()
        return n
