"""
ares-api · Promptfoo Adapter (promptfoo_adapter.py)

Purpose
-------
Concrete adapter that wraps Promptfoo behind the
``BaseAdapter`` interface.

Responsibilities
----------------
- Implement ``run_attack()`` — translate PromptStrike's target
  and config into Promptfoo-compatible parameters, execute the
  evaluation, and normalise results into ``AttackResult`` objects.
- Implement ``cancel()`` — terminate the Promptfoo process.
- Implement ``get_status()`` — report current execution state.

Integration Notes
-----------------
Promptfoo is a Node.js-based tool. The most likely integration
strategies are:
    1. CLI subprocess — invoke ``npx promptfoo eval ...`` as a
       child process and parse stdout/file output.
    2. REST API — if Promptfoo exposes a server mode, call it
       over HTTP.
The team should evaluate which approach provides the best
balance of reliability and real-time progress feedback.

Key Interfaces
--------------
    class PromptfooAdapter(BaseAdapter):
        async def run_attack(target, config) -> list[AttackResult]: ...
        async def cancel() -> None: ...
        async def get_status() -> str: ...
"""
