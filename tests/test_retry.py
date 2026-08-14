from northstar_metrics.retry import next_delay


def test_delay_caps() -> None:
    assert next_delay(1) == 0.25
    assert next_delay(8) == 4.0
