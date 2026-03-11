# ares-api — PromptStrike Backend

> **Codename: Ares** *(God of War)* — Attack orchestration engine and API layer for PromptStrike.

PromptStrike is a web-based cybersecurity platform built for the **Transformation and Decision Analysis Center (TDAC)** that enables analysts to test Large Language Models for prompt injection vulnerabilities.  This repository contains the backend API, responsible for orchestrating attacks via Garak, Promptfoo, and ChainForge, managing assessment lifecycles, enforcing authentication and RBAC, and persisting all data to PostgreSQL.

**Frontend companion repo:** [`promptStrike-hermes-client`](https://github.com/Escanor4323/promptStrike-hermes-client) (SvelteKit)

---

## Tech Stack

| Component        | Technology                           |
|------------------|--------------------------------------|
| Language         | Python 3.11+                         |
| Framework        | FastAPI                              |
| ORM              | SQLAlchemy 2.0 (async via `asyncpg`) |
| Migrations       | Alembic                              |
| Database         | PostgreSQL 16                        |
| PDF Export       | WeasyPrint                           |
| Real-Time        | Server-Sent Events (SSE)             |
| Containerization | Docker / Docker Compose              |
| Target OS        | Kali Linux                           |

---

## Architecture

The backend follows a **layered architecture** with strict dependency rules:

```
┌─────────────────────────────────────────────────────┐
│  Router Layer — Thin HTTP handlers (validate → respond) │
├─────────────────────────────────────────────────────┤
│  Middleware — Authentication · RBAC · Request logging    │
├─────────────────────────────────────────────────────┤
│  Service Layer — All business logic and orchestration    │
├──────────────────────┬──────────────────────────────┤
│  Adapter Layer       │  Repository Layer             │
│  Garak · Promptfoo   │  All SQL / DB access          │
│  ChainForge wrappers │                               │
├──────────────────────┴──────────────────────────────┤
│                   PostgreSQL                         │
└─────────────────────────────────────────────────────┘
```

**Layer rules:**

- **Routers** never contain business logic — parse the request, call a service, return the response.
- **Services** never write raw SQL or know about HTTP status codes — operate on domain models and raise domain exceptions.
- **Repositories** are the only layer that touches the database — one repository per aggregate root.
- **Adapters** normalize external tool interfaces behind a common contract (`BaseAdapter`).
- **Middleware** handles cross-cutting concerns (auth, RBAC) before the request reaches a router.

---

## Directory Structure

```
ares-api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app factory, router/middleware registration
│   ├── config.py               # pydantic-settings: DATABASE_URL, SESSION_SECRET, etc.
│   ├── dependencies.py         # Depends() callables: get_db, get_current_user
│   │
│   ├── middleware/
│   │   ├── authentication.py   # Session cookie extraction and validation
│   │   └── authorization.py    # RBAC role-level gate
│   │
│   ├── routers/
│   │   ├── auth.py             # POST login, POST logout, GET me
│   │   ├── projects.py         # CRUD, import, export
│   │   ├── targets.py          # CSV ingest, connectivity check, list
│   │   ├── assessments.py      # Configure, execute, pause, resume, SSE stream
│   │   └── reports.py          # Generate, list, download
│   │
│   ├── services/
│   │   ├── user_service.py     # Account management, authentication
│   │   ├── project_service.py  # Project lifecycle, import/export
│   │   ├── target_service.py   # CSV parsing, connectivity, LLM detection
│   │   ├── assessment_service.py  # State machine, adapter orchestration
│   │   └── report_service.py   # Report generation and retrieval
│   │
│   ├── adapters/
│   │   ├── base_adapter.py     # Abstract interface: run_attack, cancel, get_status
│   │   ├── garak_adapter.py    # Wraps Garak vulnerability scanner
│   │   ├── promptfoo_adapter.py  # Wraps Promptfoo (Node.js-based)
│   │   └── chainforge_adapter.py # Wraps ChainForge
│   │
│   ├── models/
│   │   ├── domain.py           # SQLAlchemy ORM models (7 entities, 5 enums)
│   │   └── schemas.py          # Pydantic request/response schemas
│   │
│   ├── repositories/
│   │   ├── base.py             # Generic CRUD helpers
│   │   ├── user_repo.py
│   │   ├── project_repo.py
│   │   ├── target_repo.py
│   │   └── assessment_repo.py
│   │
│   └── utils/
│       ├── csv_parser.py       # Parse analyst-uploaded CSV of LLM URLs
│       ├── html_analyzer.py    # Auto-detect LLM type from page HTML
│       ├── pdf_generator.py    # Render PDF/HTML reports via WeasyPrint
│       └── connectivity.py     # Verify target URL reachability
│
├── migrations/
│   ├── alembic.ini             # Alembic configuration
│   ├── env.py                  # Migration environment (points to domain models)
│   └── versions/               # Auto-generated migration scripts
│
├── tests/
│   ├── conftest.py             # Shared fixtures: test DB, client, factories
│   ├── unit/
│   └── integration/
│
├── docs/
│   └── architechture_overview.md
│
├── Dockerfile                  # Commented outline (team finalizes)
├── docker-compose.yml          # Commented outline: ares-api + postgres + optional redis
├── pyproject.toml              # Project metadata and dependencies
├── .env.example                # Template for required environment variables
├── .gitignore
└── .dockerignore
```

---

## API Routes

All routes are prefixed with `/api/v1` and use **kebab-case** paths.

| Module       | Endpoints |
|--------------|-----------|
| **Auth**     | `POST /auth/login` · `POST /auth/logout` · `GET /auth/me` |
| **Projects** | `GET /projects` · `POST /projects` · `GET/PUT/DELETE /projects/{id}` · `POST /projects/import` · `GET /projects/{id}/export` |
| **Targets**  | `POST /projects/{id}/targets/ingest` · `GET /projects/{id}/targets` · `POST .../targets/{id}/check` · `PUT .../targets/{id}` |
| **Assessments** | `POST /assessments` · `GET /assessments/{id}` · `POST .../execute` · `POST .../pause` · `POST .../resume` · `GET .../stream` (SSE) |
| **Reports**  | `GET /projects/{id}/reports` · `POST .../reports/generate` · `GET /reports/{id}/download` |

---

## Data Model

Seven domain entities backed by PostgreSQL:

| Entity              | Purpose |
|---------------------|---------|
| **User**            | Analyst, team lead, or admin account |
| **Project**         | Container for a testing engagement |
| **Target**          | An LLM endpoint URL to be tested |
| **Assessment**      | A configured test run with lifecycle state machine |
| **AttackResult**    | A single prompt-response pair from an attack |
| **AttackTemplate**  | A reusable, analyst-defined attack configuration |
| **Report**          | A generated PDF or HTML report artifact |

**Enums:** `UserRole` (admin, team_lead, analyst) · `AssessmentType` (cvi, cvpa) · `ProjectStatus` (created, active, archived, deleted) · `AssessmentStatus` (pending, running, paused, completed, failed) · `ReportFormat` (pdf, html)

**Assessment state machine:**

```
Pending ──execute──▸ Running ──complete──▸ Completed
                     Running ──error────▸  Failed
                     Running ──pause───▸   Paused ──resume──▸ Running
```

---

## Setup

### Prerequisites

- Docker & Docker Compose
- Python 3.11+ (for local development without Docker)
- PostgreSQL 16 (if running locally)

### Quick Start (Docker)

```bash
# 1. Clone the repository
git clone https://github.com/Escanor4323/promptStrike-ares-api.git
cd promptStrike-ares-api

# 2. Copy and configure environment variables
cp .env.example .env
# Edit .env with your actual secrets and database credentials

# 3. Start the full stack
docker compose up --build

# 4. API available at http://localhost:8000
# 5. Interactive docs at http://localhost:8000/docs
```

### Local Development (without Docker)

```bash
# 1. Create and activate a virtual environment
python3.11 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -e ".[dev]"

# 3. Set up environment variables
cp .env.example .env

# 4. Run database migrations
alembic upgrade head

# 5. Start the development server
uvicorn app.main:app --reload --port 8000

# 6. Run tests
pytest
```

---

## Environment Variables

| Variable          | Description                          | Default |
|-------------------|--------------------------------------|---------|
| `DATABASE_URL`    | Async PostgreSQL connection string   | `postgresql+asyncpg://postgres:postgres@localhost:5432/promptstrike` |
| `SESSION_SECRET`  | Secret key for signing session cookies | *(required — generate a real secret)* |
| `SESSION_MAX_AGE` | Session TTL in seconds               | `3600` |
| `DEBUG`           | Enable debug mode                    | `true` |

See [`.env.example`](.env.example) for the full template.

---

## Naming Conventions

| Element             | Convention       | Example                    |
|---------------------|------------------|----------------------------|
| Files & modules     | `snake_case.py`  | `project_service.py`       |
| Functions & methods | `snake_case`     | `create_project()`         |
| Variables           | `snake_case`     | `attack_result`            |
| Classes             | `PascalCase`     | `ProjectService`           |
| Constants           | `UPPER_SNAKE_CASE` | `MAX_RETRIES`            |
| API route paths     | `kebab-case`     | `/api/v1/attack-templates` |
| DB table names      | `snake_case`, plural | `attack_results`       |
| DB column names     | `snake_case`     | `created_at`               |
| Env variables       | `UPPER_SNAKE_CASE` | `DATABASE_URL`           |

---

## Architecture Documentation

See [`docs/architechture_overview.md`](docs/architechture_overview.md) for:

- Container topology diagrams
- Backend layered architecture details
- Entity relationship diagram
- Assessment & project lifecycle state models
- Session management & RBAC design
- STIG CAT I compliance implications
- Design patterns used throughout the codebase

## Developer Setup — Pre-Commit Hooks

Pre-commit hooks run **automatically on every `git commit`** and block the commit if any check fails.  This is the first line of defense — CI should never fail because of lint, format, or type errors.

### One-Time Setup (after cloning)

```bash
# Install the pre-commit framework
pip install pre-commit

# Install the hooks into .git/hooks
pre-commit install

# Verify hooks are active (runs against entire repo)
pre-commit run --all-files
```

### Emergency Bypass

```bash
# Skips ALL hooks — document the reason in the commit message
git commit --no-verify -m "EMERGENCY: <reason>"
```

> [!WARNING]
> `--no-verify` bypasses **all** pre-commit hooks.  Use only in genuine emergencies.  CI will still catch violations — this just skips the local gate.

### Developer Convenience (Makefile)

Run checks manually at any time:

```bash
make lint          # ruff check app/ tests/ --fix
make format        # ruff format app/ tests/
make typecheck     # mypy app/
make test          # pytest tests/unit/ -v -x
make test-all      # pytest tests/ -v
make check         # lint + format + typecheck (mirrors pre-commit)
make install-hooks # pre-commit install
```

---

## Standard Operating Procedure — Commit Workflow

```
1. Write code
2. Stage changes:           git add <files>
3. Commit:                  git commit -m "descriptive message"
   → Pre-commit hooks run automatically:
     a. ruff check (lint — auto-fixes where possible)
     b. ruff format (format — auto-fixes in place)
     c. mypy (type check — no auto-fix, you must correct manually)
     d. Whitespace, EOF, YAML, large file, private key checks
   → If any hook fails:
     • Auto-fixable: files are modified. Re-stage (git add) and re-commit.
     • Manual fix required: read the error, fix the code, re-stage, re-commit.
4. Push to remote:          git push origin <branch>
5. CI pipeline runs full suite (lint + types + unit + integration)
6. Open PR when ready → CI must pass → 1 review required → merge
```

---

## Commit Message Convention

We follow **[Conventional Commits](https://www.conventionalcommits.org/)**:

```
<type>(<scope>): <short description>
```

| Type       | Use When                                               |
|------------|--------------------------------------------------------|
| `feat`     | New feature                                            |
| `fix`      | Bug fix                                                |
| `refactor` | Code change that neither fixes a bug nor adds a feature|
| `docs`     | Documentation only                                     |
| `test`     | Adding or updating tests                               |
| `chore`    | Build, CI, dependency updates                          |
| `style`    | Formatting, whitespace (no logic change)               |

**Scope** *(optional)*: `router`, `service`, `adapter`, `model`, `middleware`, `config`

**Examples:**

```
feat(router): add project CRUD endpoints
fix(service): enforce state transition validation in assessment_service
test(repo): add integration tests for project_repo
chore(ci): add mypy to pre-commit hooks
```

> [!NOTE]
> Commit message format is a **team convention** — it is not enforced by a hook.  A `commitlint` hook can be added later if the team wants enforcement.

---

## Team

**Team 11 (TrailDev)** · CS 4310 Software Engineering · UTEP

---

## License

All components are FOSS — no paid licensing (per RDD Req #9).
