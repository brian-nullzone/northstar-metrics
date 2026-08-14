# Review backlog

Obvious leftovers. Not the tag-key contract.

- `scripts/quality_gate.py` always writes a receipt and exits 0.
- `scripts/check.sh` runs black/mypy with `|| true`.
- `tools/code_policies.go` never opens the paths it prints as scanned.
- `docs/dashboard.html` still says queue depth 3 / error 0.4%.
