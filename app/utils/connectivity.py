"""
ares-api · Connectivity Checker (connectivity.py)

Purpose
-------
Verify whether a target LLM URL is reachable and measure
response latency.

Responsibilities
----------------
- Send an HTTP HEAD request (falling back to GET if HEAD is
  not supported) to the target URL with a configurable timeout.
- Return a result containing:
    • ``reachable`` (bool) — whether the request succeeded.
    • ``status_code`` (int | None) — HTTP status code received.
    • ``latency_ms`` (int | None) — round-trip time in
      milliseconds.
- Handle errors gracefully: DNS failures, timeouts, connection
  refused, TLS errors, etc. should all result in
  ``reachable=False`` with a descriptive error message rather
  than an unhandled exception.

Key Interfaces
--------------
    @dataclass
    class ConnectivityResult:
        reachable: bool
        status_code: int | None
        latency_ms: int | None
        error: str | None

    async def check_connectivity(
        url: str, timeout_seconds: float = 10.0,
    ) -> ConnectivityResult:
        ...
"""
