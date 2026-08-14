from northstar_metrics.buffer import EventBuffer


def test_buffer_add_and_clear() -> None:
    b = EventBuffer()
    b.add({"name": "a"})
    assert len(b) == 1
    assert b.clear() == 1
    assert len(b) == 0
