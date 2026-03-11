"""
ares-api · Assessment Repository (assessment_repo.py)

Purpose
-------
Data-access layer for the ``Assessment`` and ``AttackResult``
entities. Only module that should execute SQL queries against
the ``assessments`` and ``attack_results`` tables.

Responsibilities
----------------
- ``create_assessment(assessment)`` — insert a new assessment.
- ``get_by_id(assessment_id)`` — fetch an assessment with its
  related attack results eagerly loaded.
- ``update_status(assessment_id, new_status)`` — update the
  assessment's ``AssessmentStatus``.
- ``list_by_project(project_id)`` — all assessments in a
  project.
- ``bulk_create_results(results)`` — insert multiple
  ``AttackResult`` records in one transaction.

Key Interfaces
--------------
    class AssessmentRepository(BaseRepository):
        async def create_assessment(
            self, assessment: Assessment,
        ) -> Assessment: ...
        async def get_by_id(
            self, assessment_id: UUID,
        ) -> Assessment | None: ...
        async def update_status(
            self, assessment_id: UUID,
            status: AssessmentStatus,
        ) -> None: ...
        async def list_by_project(
            self, project_id: UUID,
        ) -> list[Assessment]: ...
        async def bulk_create_results(
            self, results: list[AttackResult],
        ) -> None: ...
"""
