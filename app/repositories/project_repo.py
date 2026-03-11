"""
ares-api · Project Repository (project_repo.py)

Purpose
-------
Data-access layer for the ``Project`` entity. Only module that
should execute SQL queries against the ``projects`` table.

Responsibilities
----------------
- ``list_by_owner(owner_id)`` — projects owned by a specific
  user.
- ``get_by_id(project_id)`` — fetch a single project.
- ``create(project)`` — insert a new project record.
- ``update(project_id, data)`` — update project fields.
- ``delete(project_id)`` — soft-delete / archive a project.
- ``check_duplicate(owner_id, name)`` — return ``True`` if a
  project with the same name exists for this owner.

Key Interfaces
--------------
    class ProjectRepository(BaseRepository):
        async def list_by_owner(self, owner_id: UUID) -> list[Project]: ...
        async def get_by_id(self, project_id: UUID) -> Project | None: ...
        async def create(self, project: Project) -> Project: ...
        async def update(self, project_id: UUID, data: dict) -> Project: ...
        async def delete(self, project_id: UUID) -> None: ...
        async def check_duplicate(self, owner_id: UUID, name: str) -> bool: ...
"""
