"""
ares-api · Project Service (project_service.py)

Purpose
-------
Business logic for PromptStrike project lifecycle. Enforces
ownership and role-scoping rules. HTTP-agnostic.

Responsibilities
----------------
- ``create_project(owner, name, description)`` — Validate input,
  check for duplicate project names for the owner, persist via
  ``project_repo``.
- ``list_projects(user)`` — Return projects visible to the user.
  Admins see all; team leads see their team's; analysts see only
  their own.
- ``update_project(project_id, data)`` — Update metadata fields.
- ``delete_project(project_id)`` — Soft-delete or archive. Must
  verify ownership / admin role before deletion.
- ``import_project(file_data)`` — Deserialise an exported
  project archive and recreate project + targets + assessments.
- ``export_project(project_id)`` — Serialise the project with
  all related data into a downloadable archive.

Key Interfaces
--------------
    class ProjectService:
        async def create_project(...) -> Project: ...
        async def list_projects(user: User) -> list[Project]: ...
        async def update_project(...) -> Project: ...
        async def delete_project(project_id: UUID) -> None: ...
        async def import_project(file_data: bytes) -> Project: ...
        async def export_project(project_id: UUID) -> bytes: ...
"""
