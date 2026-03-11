"""
ares-api · User Service (user_service.py)

Purpose
-------
Business logic for user account management. This service is
HTTP-agnostic — it receives and returns domain objects, never
``Request`` or ``Response``.

Responsibilities
----------------
- ``create_user(username, password, role)`` — Hash the password
  (bcrypt), persist via ``user_repo``, return the new user.
- ``authenticate(username, password)`` — Look up the user by
  username, verify the password hash, return the user on success
  or raise a domain exception on failure.
- ``get_by_id(user_id)`` — Retrieve a single user by primary
  key.
- ``update_role(user_id, new_role)`` — Change a user's
  ``UserRole``. Only admins should be allowed to call this
  (enforced at the router/middleware level).

Key Interfaces
--------------
    class UserService:
        async def create_user(...) -> User: ...
        async def authenticate(...) -> User: ...
        async def get_by_id(user_id: UUID) -> User: ...
        async def update_role(user_id: UUID, role: UserRole) -> User: ...
"""
