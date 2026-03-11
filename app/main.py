"""
ares-api · Application Entry Point (main.py)

Purpose
-------
FastAPI application factory. Creates and configures the top-level
``FastAPI`` instance, registers all routers (with the ``/api/v1``
prefix), and attaches middleware.

Responsibilities
----------------
- Instantiate the ``FastAPI`` application with metadata (title,
  version, description, docs URL).
- Register the authentication and authorization middleware (from
  ``app.middleware``).
- Include every router defined in ``app.routers`` under the
  ``/api/v1`` prefix.
- Optionally configure CORS, trusted-host, and gzip middleware.
- Expose a ``/healthz`` endpoint for container health checks.

Key Interfaces
--------------
    app = create_app() -> FastAPI
        Factory function that builds and returns the configured
        FastAPI application instance.
"""
