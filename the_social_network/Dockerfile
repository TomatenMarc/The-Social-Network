FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk add --virtual build-deps curl gcc python3-dev musl-dev openssl-dev libffi-dev build-base linux-headers && \
    apk add jpeg-dev zlib-dev libjpeg pcre-dev
WORKDIR /code
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry install
COPY . ./
RUN apk del build-deps
