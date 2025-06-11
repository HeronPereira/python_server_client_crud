FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir httpx pydantic-settings pydantic[email]

CMD ["python", "client.py"]
