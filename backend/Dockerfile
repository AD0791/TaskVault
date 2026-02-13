FROM python:3.12-slim

WORKDIR /app

# Install uv (ultra-fast Python package manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install dependencies via uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Copy application code
COPY app/ ./app/

# Create data directory for SQLite
RUN mkdir -p /data

EXPOSE 8000

# Run with --reload for dev (watches /app/app/ for changes via volume mount)
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
