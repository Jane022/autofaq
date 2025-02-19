
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright

RUN apt-get update && \
    apt-get install -y \
    gcc \
    python3-dev \
    libgstreamer1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    libxss1 \
    libnss3 \
    libxrandr2 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libgbm1 \
    wget \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip && \
    pip install playwright pytest

RUN playwright install

RUN playwright install --with-deps firefox

RUN pip install -r requirements.txt


COPY . .

CMD ["pytest", "-v"]