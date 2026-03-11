"""
ares-api · Authentication Middleware (authentication.py)

Purpose
-------
ASGI middleware that intercepts every incoming request, extracts
the session cookie, and validates it before the request reaches
any route handler.

Responsibilities
----------------
- Read the session cookie (name configurable via ``Settings``).
- Decode / verify the cookie signature using ``SESSION_SECRET``.
- Reject expired sessions (compare against ``SESSION_MAX_AGE``).
- Attach the authenticated user identity to ``request.state``
  so downstream dependencies and route handlers can access it.
- Return ``401 Unauthorized`` for missing or invalid session
  cookies on protected routes.
- Allow a configurable list of public paths (e.g., ``/healthz``,
  ``/api/v1/auth/login``) to bypass authentication.

Key Interfaces
--------------
    class AuthenticationMiddleware(BaseHTTPMiddleware):
        async def dispatch(
            self, request: Request, call_next: Callable,
        ) -> Response: ...
"""
