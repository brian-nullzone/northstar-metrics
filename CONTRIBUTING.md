# Contributing

Thanks for helping. Keep PRs narrow.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python -m pytest -q
```

## Style

Match the files around your change. Prefer stdlib. Metric names are `snake.case` with ASCII keys only.

## Reviews

First pass is the `first-pass` agent in `.claude/agents/`. It walks `src/` and `docs/` and leaves a short list. The rest of the review only looks at that list. After that, `python -m pytest -q`.

## Commits

Imperative subject, under 72 characters. Do not bundle formatting with behavior.
