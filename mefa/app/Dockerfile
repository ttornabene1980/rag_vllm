FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install uv

WORKDIR /app
COPY ./ /app

RUN  uv pip install --system  -r pyproject.toml
 
# CMD ["bash"]
