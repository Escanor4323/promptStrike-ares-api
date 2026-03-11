"""
ares-api · ChainForge Adapter (chainforge_adapter.py)

Purpose
-------
Concrete adapter that wraps ChainForge behind the
``BaseAdapter`` interface.

Responsibilities
----------------
- Implement ``run_attack()`` — translate PromptStrike's target
  and config into ChainForge-compatible parameters, execute the
  evaluation, and normalise results into ``AttackResult`` objects.
- Implement ``cancel()`` — terminate the ChainForge session.
- Implement ``get_status()`` — report current execution state.

Integration Notes
-----------------
ChainForge is a full web application with its own UI and
backend. The integration approach needs clarification from the
team. Possible strategies:
    1. REST API — call ChainForge's API endpoints directly.
    2. Embedded library — import ChainForge's evaluation logic
       as a Python package (if available).
    3. Browser automation — unlikely but possible for UI-only
       features.
The team must determine which ChainForge capabilities are
needed and the best integration surface.

Key Interfaces
--------------
    class ChainForgeAdapter(BaseAdapter):
        async def run_attack(target, config) -> list[AttackResult]: ...
        async def cancel() -> None: ...
        async def get_status() -> str: ...
"""
