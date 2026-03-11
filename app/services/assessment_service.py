"""
ares-api · Assessment Service (assessment_service.py)

Purpose
-------
Core business logic for assessment lifecycle management.
Enforces the assessment state machine and coordinates attack
execution through tool adapters. HTTP-agnostic.

Responsibilities
----------------
- ``create(project_id, config)`` — Create a new assessment in
  ``Pending`` status.
- ``execute(assessment_id)`` — Transition ``Pending → Running``.
  Select the appropriate adapter (Garak, Promptfoo, ChainForge),
  launch the attack, and stream progress events.
- ``pause(assessment_id)`` — Transition ``Running → Paused``.
  Signal the adapter to suspend execution.
- ``resume(assessment_id)`` — Transition ``Paused → Running``.
  Resume the adapter.
- ``on_complete(assessment_id, results)`` — Transition
  ``Running → Completed``. Persist attack results.
- ``on_error(assessment_id, error)`` — Transition
  ``Running → Failed``. Record the error.

State Machine
-------------
    Pending  ──execute──▸  Running
    Running  ──pause───▸   Paused
    Paused   ──resume──▸   Running
    Running  ──complete─▸  Completed
    Running  ──error────▸  Failed

Invalid transitions must raise a domain exception.

Key Interfaces
--------------
    class AssessmentService:
        async def create(...) -> Assessment: ...
        async def execute(assessment_id: UUID) -> None: ...
        async def pause(assessment_id: UUID) -> None: ...
        async def resume(assessment_id: UUID) -> None: ...
        async def on_complete(assessment_id: UUID, results: ...) -> None: ...
        async def on_error(assessment_id: UUID, error: str) -> None: ...
"""
