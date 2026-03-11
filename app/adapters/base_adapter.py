"""
ares-api · Base Adapter (base_adapter.py)

Purpose
-------
Abstract base class that defines the contract all tool adapters
must implement. Ensures a uniform interface regardless of the
underlying attack tool (Garak, Promptfoo, ChainForge, or future
integrations).

Responsibilities
----------------
- Declare the abstract methods that every concrete adapter must
  override.
- Serve as a type-hint interface for the service layer so it
  can work with any adapter polymorphically.

Key Interfaces
--------------
    class BaseAdapter(ABC):

        @abstractmethod
        async def run_attack(
            self, target: Target, config: dict,
        ) -> list[AttackResult]:
            \"\"\"Execute attacks against the target using the
            adapter's underlying tool. Return normalised results.\"\"\"
            ...

        @abstractmethod
        async def cancel(self) -> None:
            \"\"\"Signal the underlying tool to stop execution.\"\"\"
            ...

        @abstractmethod
        async def get_status(self) -> str:
            \"\"\"Return the current execution status of the tool
            (e.g., 'running', 'idle', 'error').\"\"\"
            ...
"""
