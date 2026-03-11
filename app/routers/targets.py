"""
ares-api · Targets Router (targets.py)

Purpose
-------
Endpoints for managing LLM targets within a project. Handles
CSV ingest, connectivity checks, and target metadata updates.

Responsibilities
----------------
- ``POST /api/v1/projects/{project_id}/targets/ingest``
      Accept a CSV file upload, parse it via ``csv_parser``,
      and delegate to ``target_service.ingest_csv()``.
- ``GET  /api/v1/projects/{project_id}/targets``
      List all targets belonging to the given project.
- ``POST /api/v1/projects/{project_id}/targets/{target_id}/check``
      Trigger a connectivity check for a single target.
- ``PUT  /api/v1/projects/{project_id}/targets/{target_id}``
      Update target metadata (e.g., display name, notes).

Key Interfaces
--------------
    router = APIRouter(
        prefix="/api/v1/projects/{project_id}/targets",
        tags=["targets"],
    )
"""
