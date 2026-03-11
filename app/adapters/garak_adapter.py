"""
ares-api · Garak Adapter (garak_adapter.py)

Purpose
-------
Concrete adapter that wraps the Garak LLM vulnerability
scanner behind the ``BaseAdapter`` interface.

Responsibilities
----------------
- Implement ``run_attack()`` — translate PromptStrike's target
  and config into Garak-compatible parameters, execute the scan,
  and normalise results into ``AttackResult`` objects.
- Implement ``cancel()`` — terminate the Garak process or
  session.
- Implement ``get_status()`` — report whether Garak is idle,
  running, or in an error state.

Integration Notes
-----------------
The integration approach is TBD and should be decided by the
team. Possible strategies:
    1. CLI subprocess — spawn ``garak`` as a child process.
    2. Library import — import ``garak`` as a Python package.
    3. Co-deployed service — call a sidecar Garak REST/gRPC
       endpoint.

Key Interfaces
--------------
    class GarakAdapter(BaseAdapter):
        async def run_attack(target, config) -> list[AttackResult]: ...
        async def cancel() -> None: ...
        async def get_status() -> str: ...
"""
