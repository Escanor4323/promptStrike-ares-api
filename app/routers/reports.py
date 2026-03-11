"""
ares-api · Reports Router (reports.py)

Purpose
-------
Endpoints for generating, listing, and downloading assessment
reports in PDF or HTML format.

Responsibilities
----------------
- ``GET  /api/v1/projects/{project_id}/reports``
      List all reports belonging to the given project.
- ``POST /api/v1/projects/{project_id}/reports/generate``
      Trigger report generation for one or more assessments.
      Delegates to ``report_service.generate_report()``.
- ``GET  /api/v1/reports/{report_id}/download``
      Download a generated report file (PDF or HTML).

Key Interfaces
--------------
    router = APIRouter(tags=["reports"])

    # Routes are split across two prefixes:
    #   /api/v1/projects/{project_id}/reports   (list, generate)
    #   /api/v1/reports/{report_id}/download    (download)
"""
