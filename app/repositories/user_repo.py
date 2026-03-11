"""
ares-api · User Repository (user_repo.py)

Purpose
-------
Data-access layer for the ``User`` entity. This is the only
module that should execute SQL queries against the ``users``
table.

Responsibilities
----------------
- ``get_by_username(username)`` — look up a user by their unique
  username (used during login).
- ``get_by_id(user_id)`` — fetch a user by primary key.
- ``create(user)`` — insert a new user record.
- ``update_role(user_id, new_role)`` — change the user's role.
- ``list_all()`` — return all users (admin-only operation).

Key Interfaces
--------------
    class UserRepository(BaseRepository):
        async def get_by_username(self, username: str) -> User | None: ...
        async def get_by_id(self, user_id: UUID) -> User | None: ...
        async def create(self, user: User) -> User: ...
        async def update_role(self, user_id: UUID, role: UserRole) -> User: ...
        async def list_all(self) -> list[User]: ...
"""
