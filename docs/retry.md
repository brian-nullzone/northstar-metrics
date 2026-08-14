# Retry

`next_delay(attempt)` doubles from 0.25s and caps at 4s. The client does not retry on its own; callers can.
