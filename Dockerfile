FROM python:3-slim-buster

COPY requirements.txt /tmp/
COPY src/.*  /app

RUN apt-get update \
    && python3 -m pip install -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt

CMD ['python3 --version']