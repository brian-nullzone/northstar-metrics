# northstar-metrics

Small Python client for emitting product metrics from worker processes. Not a hosted service — you point it at your own collector.

## Install

```bash
pip install -e .
```

## Usage

```python
from northstar_metrics import Client

client = Client(endpoint="http://127.0.0.1:9090/v1/events")
client.count("payment.ack", tags={"queue": "payments"})
client.flush()
```

## Development

```bash
pip install -e ".[dev]"
python -m pytest -q
```

See `CONTRIBUTING.md`. Notes for reviewers live in `docs/`.

## Layout

```
src/northstar_metrics/   client
scripts/                 local checks
tools/
tests/
docs/
```
