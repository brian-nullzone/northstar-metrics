# Daily notes

Setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m pytest -q
```

Local preflight is `scripts/check.sh`. Review process is in `CONTRIBUTING.md`.
