"""
ares-api · Domain Models (domain.py)

Purpose
-------
SQLAlchemy 2.0 ORM table-mapped classes representing the
PromptStrike domain. Each class maps to a PostgreSQL table
(``snake_case``, plural). **Do NOT define the classes here
yet** — this docstring documents what the team should build.

Entities to Implement
---------------------
1. **User**
   - Represents an analyst, team lead, or admin account.
   - Columns: ``id`` (UUID PK), ``username`` (unique),
     ``password_hash``, ``role`` (UserRole enum), ``created_at``,
     ``updated_at``.

2. **Project**
   - A container for a testing engagement.
   - Columns: ``id``, ``name``, ``description``, ``owner_id``
     (FK → users), ``status`` (ProjectStatus enum),
     ``created_at``, ``updated_at``.

3. **Target**
   - An LLM endpoint URL to be tested.
   - Columns: ``id``, ``project_id`` (FK), ``url``, ``name``,
     ``llm_type`` (nullable), ``is_reachable`` (bool),
     ``latency_ms`` (nullable int), ``created_at``.

4. **Assessment**
   - A configured test run against one or more targets.
   - Columns: ``id``, ``project_id`` (FK), ``name``,
     ``assessment_type`` (AssessmentType enum), ``status``
     (AssessmentStatus enum), ``config_json`` (JSONB),
     ``started_at``, ``completed_at``, ``created_at``.

5. **AttackResult**
   - A single result from an attack probe.
   - Columns: ``id``, ``assessment_id`` (FK), ``target_id`` (FK),
     ``template_id`` (FK, nullable), ``payload``, ``response``,
     ``success`` (bool), ``created_at``.

6. **AttackTemplate**
   - A reusable attack prompt template.
   - Columns: ``id``, ``name``, ``category``, ``template_text``,
     ``created_at``.

7. **Report**
   - A generated report artifact for a project.
   - Columns: ``id``, ``project_id`` (FK), ``format``
     (ReportFormat enum), ``file_path``, ``generated_at``.

Enums to Define
---------------
- ``UserRole``         — admin, team_lead, analyst
- ``AssessmentType``   — cvi, cvpa
- ``ProjectStatus``    — created, active, archived, deleted
- ``AssessmentStatus`` — pending, running, paused, completed,
                         failed
- ``ReportFormat``     — pdf, html

Implementation Notes
--------------------
- Use ``sqlalchemy.orm.DeclarativeBase`` (SA 2.0 style).
- Use ``Mapped[]`` and ``mapped_column()`` for type-safe column
  declarations.
- All primary keys should be ``UUID`` with ``server_default``
  using ``gen_random_uuid()`` (PostgreSQL).
- Use ``sqlalchemy.Enum`` backed by Python ``enum.Enum`` for
  status/role/type columns.
"""
