# ──────────────────────────────────────────────────────────────
# Makefile — developer convenience targets for ares-api
# Usage:  make <target>
# ──────────────────────────────────────────────────────────────

.PHONY: lint format typecheck test test-all check install-hooks

## Lint Python source with ruff (auto-fix enabled)
lint:
	ruff check app/ tests/ --fix

## Format Python source with ruff
format:
	ruff format app/ tests/

## Run mypy type checking on the app package
typecheck:
	mypy app/

## Run unit tests only (fast feedback loop)
test:
	pytest tests/unit/ -v -x

## Run the full test suite (unit + integration)
test-all:
	pytest tests/ -v

## Run all static-analysis checks (mirrors pre-commit)
check: lint format typecheck

## Install pre-commit hooks into .git/hooks
install-hooks:
	pre-commit install
