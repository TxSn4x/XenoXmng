FROM python:3.10-slim-bullseye

# System deps
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    gnupg \
    ffmpeg \
    aria2 \
    && rm -rf /var/lib/apt/lists/*

# Node.js 18 LTS (last safe version)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g yarn \
    && npm cache clean --force

WORKDIR /app
COPY . /app

# Python deps
RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

CMD ["bash", "start"]
