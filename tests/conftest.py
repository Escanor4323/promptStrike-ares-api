"""
ares-api · Test Configuration & Shared Fixtures (conftest.py)

Purpose
-------
Pytest fixtures shared across all test modules. Sets up the
test database, async test client, factory helpers, and mock
adapters.

Fixtures to Implement
---------------------
- ``test_db`` — create a disposable PostgreSQL database (or use
  an in-memory SQLite with ``aiosqlite`` for speed), run
  migrations, yield an ``AsyncSession``, then tear down.
- ``test_client`` — ``httpx.AsyncClient`` configured with the
  FastAPI ``TestClient`` (via ``ASGITransport``) so tests can
  call API endpoints without a running server.
- ``user_factory`` — helper function that creates ``User``
  records with sensible defaults (useful in both unit and
  integration tests).
- ``project_factory`` — helper that creates ``Project`` records.
- ``mock_adapter`` — a ``BaseAdapter`` subclass with
  pre-programmed return values and call tracking, so service
  tests can run without real tool binaries.

Configuration
-------------
- Use ``pytest-asyncio`` with ``asyncio_mode = "auto"`` for
  seamless async test support.
- Override ``get_db`` and ``get_current_user`` dependencies in
  the test app to inject the test session and a fake user.
"""
