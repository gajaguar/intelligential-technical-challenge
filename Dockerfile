# Base stage
FROM python:3.10-alpine as base

WORKDIR /code

# Development stage
FROM base AS development

# Production stage
FROM base AS production

COPY . .

CMD ["python", "/code/app/main.py"]
