# Use a slim Python image
FROM python:3.12-slim

# Install uv for high-performance dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv sync (installs into .venv by default)
# We use --frozen to ensure lockfile consistency
RUN uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application code
COPY . .

# Ensure data directory exists for SQLite
RUN mkdir -p data

# Expose the API port
EXPOSE 8000

# Set the entry point to run with uvicorn and multiple workers
# This matches the production scaling we defined earlier
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
