FROM python:3.10.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY --chmod=777 entrypoint.sh .
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD sh entrypoint.sh