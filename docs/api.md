# Client

`Client(endpoint, timeout_s=2.0)` buffers `count()` calls and `flush()` POSTs JSON.

On `OSError` the buffer is kept. There is no max size.
