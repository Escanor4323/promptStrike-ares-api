"""
ares-api · FastAPI Dependencies (dependencies.py)

Purpose
-------
Reusable ``Depends()`` callables injected into route handlers.
Keeps dependency wiring in a single place so routers stay thin.

Responsibilities
----------------
- ``get_db()`` — async generator that yields a SQLAlchemy
  ``AsyncSession`` from the engine/session-maker and ensures the
  session is closed after the request.
- ``get_current_user()`` — extracts and validates the session
  cookie / token, queries the user from the database, and returns
  the authenticated ``User`` domain object. Raises
  ``HTTPException(401)`` on invalid or missing credentials.

Key Interfaces
--------------
    async def get_db() -> AsyncGenerator[AsyncSession, None]: ...

    async def get_current_user(
        session: AsyncSession = Depends(get_db),
    ) -> User: ...
"""
