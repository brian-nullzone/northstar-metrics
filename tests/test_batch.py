from northstar_metrics.batch import chunks


def test_chunks() -> None:
    assert chunks([{"n": 1}, {"n": 2}, {"n": 3}], 2) == [[{"n": 1}, {"n": 2}], [{"n": 3}]]
