"""
ares-api · Application Configuration (config.py)

Purpose
-------
Centralised, validated configuration using ``pydantic-settings``.
All environment variables are loaded here and exposed as typed
attributes on a singleton ``Settings`` object.

Responsibilities
----------------
- Define a ``Settings`` class inheriting from
  ``pydantic_settings.BaseSettings``.
- Declare and validate the following environment variables:
    • DATABASE_URL  (str)  — async PostgreSQL connection string
    • SESSION_SECRET (str) — secret key for signing session cookies
    • SESSION_MAX_AGE (int, default 3600) — session TTL in seconds
    • DEBUG (bool, default False) — toggle debug mode
- Provide a cached ``get_settings()`` function (using
  ``functools.lru_cache``) so a single instance is shared
  application-wide.

Key Interfaces
--------------
    class Settings(BaseSettings): ...

    def get_settings() -> Settings: ...
"""
