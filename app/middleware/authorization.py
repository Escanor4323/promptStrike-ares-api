"""
ares-api · Authorization Middleware (authorization.py)

Purpose
-------
RBAC (Role-Based Access Control) gate that enforces role-level
permissions on API routes. Resource-level authorization (e.g.,
"does this user own this project?") is handled in the service
layer, not here.

Responsibilities
----------------
- Define a mapping of route patterns to the minimum required
  ``UserRole`` (admin, team_lead, analyst).
- After the authentication middleware has attached the user
  identity to ``request.state``, verify the user's role meets
  the requirement for the requested route.
- Return ``403 Forbidden`` when the user's role is insufficient.
- Pass the request through unmodified when authorization
  succeeds.

Key Interfaces
--------------
    class AuthorizationMiddleware(BaseHTTPMiddleware):
        async def dispatch(
            self, request: Request, call_next: Callable,
        ) -> Response: ...
"""
