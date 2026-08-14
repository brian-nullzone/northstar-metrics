from northstar_metrics.names import event_name


def test_event_name() -> None:
    assert event_name(["Payment", "Ack"]) == "payment.ack"
