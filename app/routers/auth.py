"""
ares-api · Auth Router (auth.py)

Purpose
-------
Thin HTTP layer for authentication-related endpoints. Validates
request payloads, delegates to ``user_service``, and returns
appropriate responses. No business logic belongs here.

Responsibilities
----------------
- ``POST /api/v1/auth/login``  — Accept credentials (username +
  password), call ``user_service.authenticate()``, set a signed
  session cookie on success, return ``401`` on failure.
- ``POST /api/v1/auth/logout`` — Clear the session cookie.
- ``GET  /api/v1/auth/me``     — Return the profile of the
  currently authenticated user.

Key Interfaces
--------------
    router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

    @router.post("/login")
    async def login(payload: LoginRequest, ...) -> LoginResponse:
        ...

    @router.post("/logout")
    async def logout(...) -> dict:
        ...

    @router.get("/me")
    async def me(current_user: User = Depends(...)) -> UserResponse:
        ...
"""
