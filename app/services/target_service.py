"""
ares-api · Target Service (target_service.py)

Purpose
-------
Business logic for LLM target management within a project.
Orchestrates CSV parsing, connectivity probes, and automatic
LLM type detection. HTTP-agnostic.

Responsibilities
----------------
- ``ingest_csv(project_id, csv_file)`` — Delegate file parsing
  to ``csv_parser``, deduplicate URLs, bulk-create targets in
  the database via ``target_repo``.
- ``check_connectivity(target_id)`` — Call
  ``connectivity.check()`` against the target URL, update
  reachability status and latency in the database.
- ``detect_llm_type(target_id)`` — Fetch the target URL's HTML,
  pass it to ``html_analyzer.detect()``, update the target
  record with the detected LLM type.
- ``list_targets(project_id)`` — Return all targets belonging
  to the given project.

Key Interfaces
--------------
    class TargetService:
        async def ingest_csv(
            project_id: UUID, csv_file: ...,
        ) -> list[Target]: ...
        async def check_connectivity(
            target_id: UUID,
        ) -> ConnectivityResult: ...
        async def detect_llm_type(
            target_id: UUID,
        ) -> str | None: ...
        async def list_targets(
            project_id: UUID,
        ) -> list[Target]: ...
"""
