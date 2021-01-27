FROM python:3.7.8


WORKDIR /fastapi

USER root

COPY requirements.txt .


RUN pip install -r requirements.txt

COPY app.py .

COPY run.sh .

CMD sh run.sh