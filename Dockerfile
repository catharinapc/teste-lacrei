FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
COPY poetry.lock ./
COPY README.md ./

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main --no-root

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn lacreisaude.wsgi:application --bind 0.0.0.0:8000"]