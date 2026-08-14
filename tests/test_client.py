from northstar_metrics import Client
from northstar_metrics.normalize import normalize_key


def test_buffer_count() -> None:
    c = Client(endpoint="http://127.0.0.1:9/v1/events")
    c.count("payment.ack")
    assert len(c._buf) == 1


def test_normalize() -> None:
    assert normalize_key("Payment Ack") == "payment_ack"
