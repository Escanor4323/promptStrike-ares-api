"""
ares-api · Projects Router (projects.py)

Purpose
-------
CRUD and import/export endpoints for PromptStrike projects.
Thin layer: validates input, calls ``project_service``, returns
the response.

Responsibilities
----------------
- ``GET    /api/v1/projects``
      List projects visible to the current user (scoped by
      role and ownership).
- ``POST   /api/v1/projects``
      Create a new project.
- ``GET    /api/v1/projects/{project_id}``
      Retrieve a single project by ID.
- ``PUT    /api/v1/projects/{project_id}``
      Update project metadata.
- ``DELETE /api/v1/projects/{project_id}``
      Soft-delete or archive a project.
- ``POST   /api/v1/projects/import``
      Import a project from an uploaded file.
- ``GET    /api/v1/projects/{project_id}/export``
      Export a project as a downloadable archive.

Key Interfaces
--------------
    router = APIRouter(
        prefix="/api/v1/projects", tags=["projects"],
    )
"""
