"""
ares-api · Alembic Environment Configuration (env.py)

Purpose
-------
Alembic migration environment. Configures how Alembic connects
to the database and discovers SQLAlchemy models for auto-
generating migration scripts.

Responsibilities
----------------
- Import the SQLAlchemy ``Base.metadata`` from
  ``app.models.domain`` so Alembic can detect table definitions.
- Read ``DATABASE_URL`` from the environment (or from
  ``app.config.Settings``) and configure the engine.
- Provide both ``run_migrations_offline()`` (SQL script mode)
  and ``run_migrations_online()`` (direct connection mode).
- For async support, use ``asyncpg`` together with
  ``run_async_upgrade()`` patterns (see Alembic async cookbook).

Key Interfaces
--------------
    # target_metadata should point to your ORM Base:
    # from app.models.domain import Base
    # target_metadata = Base.metadata

    def run_migrations_offline() -> None: ...
    def run_migrations_online() -> None: ...
"""
