FROM python:3.11-slim

WORKDIR /app

COPY . . 

RUN pip install --no-cache-dir fastapi uvicorn[standard] beanie motor passlib[bcrypt] python-jose pydantic-settings pydantic[email]

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]