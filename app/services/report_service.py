"""
ares-api · Report Service (report_service.py)

Purpose
-------
Business logic for assessment report generation and retrieval.
Assembles data from assessments and attack results, delegates
rendering to ``pdf_generator``. HTTP-agnostic.

Responsibilities
----------------
- ``generate_report(project_id, assessment_ids, format)``
      Gather assessment data, compile statistics (LLM count,
      attack success/fail counts, successful payloads),
      call ``pdf_generator`` to render the document, persist
      the report record, and return the report metadata.
- ``list_reports(project_id)`` — Return all reports for a
  given project.
- ``get_download_path(report_id)`` — Resolve the file-system
  path for a generated report so the router can stream the
  file back to the client.

Key Interfaces
--------------
    class ReportService:
        async def generate_report(
            project_id: UUID,
            assessment_ids: list[UUID],
            format: ReportFormat,
        ) -> Report: ...
        async def list_reports(project_id: UUID) -> list[Report]: ...
        async def get_download_path(report_id: UUID) -> Path: ...
"""
