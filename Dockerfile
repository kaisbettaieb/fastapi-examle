FROM python:3.7.8

RUN mkdir -p /usr/src/fastapi

WORKDIR /usr/src/fastapi

USER root

COPY requirements.txt /usr/src/fastapi/

RUN pip install -r requirements.txt

COPY app.py run.sh /usr/src/fastapi/

CMD sh run.sh