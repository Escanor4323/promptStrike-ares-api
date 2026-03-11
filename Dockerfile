# ─────────────────────────────────────────────────────────────
# ares-api · Dockerfile (stub)
# ─────────────────────────────────────────────────────────────
# This is a commented outline. The team should flesh it out
# once dependencies are finalized.
#
# FROM python:3.11-slim
#
# WORKDIR /app
#
# # Install system dependencies required by WeasyPrint and asyncpg
# # RUN apt-get update && apt-get install -y --no-install-recommends \
# #     libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
# #     libffi-dev libcairo2 && rm -rf /var/lib/apt/lists/*
#
# # Copy dependency manifest and install Python packages
# # COPY pyproject.toml .
# # RUN pip install --no-cache-dir .
#
# # Copy application source
# # COPY app/ app/
# # COPY migrations/ migrations/
#
# # Expose the API port
# # EXPOSE 8000
#
# # Run with Uvicorn
# # CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
