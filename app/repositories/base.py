"""
ares-api · Base Repository (base.py)

Purpose
-------
Shared session helpers and generic CRUD operations. Concrete
repositories inherit from this base to avoid duplicating common
data-access patterns.

Responsibilities
----------------
- Provide reusable methods for standard CRUD operations:
    • ``get_by_id(model, id)``  — fetch a single record by PK.
    • ``list_all(model, filters)`` — query with optional filters
      and pagination.
    • ``create(instance)`` — add and flush a new record.
    • ``update(instance, data)`` — merge updated fields.
    • ``delete(instance)`` — remove a record (or mark as soft-
      deleted depending on the model).
- Accept an ``AsyncSession`` (injected by the service layer) and
  use it for all queries — never create its own session.

Key Interfaces
--------------
    class BaseRepository:
        def __init__(self, session: AsyncSession) -> None: ...

        async def get_by_id(self, model: type[T], id: UUID) -> T | None: ...
        async def list_all(self, model: type[T], **filters) -> list[T]: ...
        async def create(self, instance: T) -> T: ...
        async def update(self, instance: T, data: dict) -> T: ...
        async def delete(self, instance: T) -> None: ...
"""
