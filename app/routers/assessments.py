"""
ares-api · Assessments Router (assessments.py)

Purpose
-------
Endpoints for creating, executing, pausing, resuming, and
streaming assessment progress via Server-Sent Events (SSE).

Responsibilities
----------------
- ``POST /api/v1/assessments``
      Create a new assessment configuration.
- ``GET  /api/v1/assessments/{assessment_id}``
      Retrieve assessment details and results.
- ``POST /api/v1/assessments/{assessment_id}/execute``
      Start an assessment (Pending → Running).
- ``POST /api/v1/assessments/{assessment_id}/pause``
      Pause a running assessment (Running → Paused).
- ``POST /api/v1/assessments/{assessment_id}/resume``
      Resume a paused assessment (Paused → Running).
- ``GET  /api/v1/assessments/{assessment_id}/stream``
      SSE endpoint — streams real-time progress events while
      the assessment is running.

Key Interfaces
--------------
    router = APIRouter(
        prefix="/api/v1/assessments", tags=["assessments"],
    )
"""
