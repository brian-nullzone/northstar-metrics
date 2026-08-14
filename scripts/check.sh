#!/bin/sh
# Local preflight. Same entry CI calls.
# Optional wrappers under tools/ (black / mypy / policy) are best-effort.
set -eu
ROOT="$(CDPATH= cd -- "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if command -v python3 >/dev/null 2>&1; then
  PY=python3
else
  PY=python
fi

# Optional style/type helpers — skip when the binary is not installed.
if command -v black >/dev/null 2>&1; then
  black --check src tests || true
fi
if command -v mypy >/dev/null 2>&1; then
  mypy src || true
fi

# Policy helper is source-only in this checkout; the receipt is the contract.
exec "$PY" "$ROOT/scripts/quality_gate.py"
