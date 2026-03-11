"""
ares-api · Target Repository (target_repo.py)

Purpose
-------
Data-access layer for the ``Target`` entity. Only module that
should execute SQL queries against the ``targets`` table.

Responsibilities
----------------
- ``list_by_project(project_id)`` — all targets for a given
  project.
- ``get_by_id(target_id)`` — fetch a single target.
- ``bulk_create(targets)`` — insert multiple targets in one
  transaction (used after CSV parsing).
- ``update_reachability(target_id, is_reachable, latency_ms)``
  — record the result of a connectivity check.
- ``update_llm_type(target_id, llm_type)`` — set the detected
  LLM type string.

Key Interfaces
--------------
    class TargetRepository(BaseRepository):
        async def list_by_project(self, project_id: UUID) -> list[Target]: ...
        async def get_by_id(self, target_id: UUID) -> Target | None: ...
        async def bulk_create(self, targets: list[Target]) -> list[Target]: ...
        async def update_reachability(
            self, target_id: UUID, is_reachable: bool, latency_ms: int | None,
        ) -> None: ...
        async def update_llm_type(self, target_id: UUID, llm_type: str) -> None: ...
"""
