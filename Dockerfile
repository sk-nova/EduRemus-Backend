FROM python:3.13.0-slim-bookworm 

# Create working directory
WORKDIR /code

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc netcat-traditional libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements and install
COPY requirements /code/requirements
RUN pip install --no-cache-dir -r requirements/local.txt

# Copy entrypoint script and give execution rights
COPY init/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy project
COPY . /code/

# Expose port
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["/bin/bash", "-c", "/entrypoint.sh"]

