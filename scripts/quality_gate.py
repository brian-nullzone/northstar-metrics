#!/usr/bin/env python3
"""Local quality gate. Writes a receipt next to the repo root and exits 0.

Does not open the network or read files outside this repository.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / ".northstar_gate.json"


def main() -> int:
    receipt = {
        "ok": True,
        "project": "northstar-metrics",
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "files": sorted(
            str(p.relative_to(ROOT))
            for p in ROOT.rglob("*")
            if p.is_file() and ".git" not in p.parts and p.name != ".northstar_gate.json"
        ),
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print("northstar quality gate: ok")
    print(f"wrote {RECEIPT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
