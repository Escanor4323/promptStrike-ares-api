"""
ares-api · Pydantic Schemas (schemas.py)

Purpose
-------
Pydantic v2 models that define the API request/response contract.
These schemas are independent of the ORM — they validate incoming
payloads and serialise outgoing responses.

Naming Convention
-----------------
Follow this pattern for every domain entity:

    <Entity>Create   — fields required to create a new record
    <Entity>Update   — fields that can be modified (all optional)
    <Entity>Response — full representation returned by the API
    <Entity>Summary  — lightweight representation for list views

Examples (do NOT implement yet — just follow the convention):

    class ProjectCreate(BaseModel): ...
    class ProjectUpdate(BaseModel): ...
    class ProjectResponse(BaseModel): ...
    class ProjectSummary(BaseModel): ...

Additional Schemas
------------------
- ``LoginRequest``  — username + password fields.
- ``LoginResponse`` — session info or token.
- ``ConnectivityResult`` — reachable (bool), status_code,
  latency_ms.
- ``PaginatedResponse[T]`` — generic wrapper with ``items``,
  ``total``, ``page``, ``page_size`` for list endpoints.

Implementation Notes
--------------------
- Use ``model_config = ConfigDict(from_attributes=True)`` on
  response schemas so they can be constructed directly from ORM
  objects.
- Reuse field validators via ``@field_validator`` for common
  patterns (e.g., URL validation, non-empty strings).
"""
