# CorpGuard FastAPI Benchmark - AgentBeats Phase 1 Competition
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml .
COPY src/ ./src/
COPY scenarios/ ./scenarios/
COPY run_battle.py ./
COPY CORPGUARD_BENCHMARK_RESULTS.md ./

# Install Python dependencies
RUN pip install --no-cache-dir -e . || pip install --no-cache-dir fastapi uvicorn httpx pydantic agentbeats

# Set PYTHONPATH to include current directory
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Expose port for FastAPI (if needed)
EXPOSE 8000

# Run the benchmark system
CMD ["python3", "run_battle.py"]
