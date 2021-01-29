FROM python:3.7.8

RUN mkdir -p /usr/src/fastapi

WORKDIR /usr/src/fastapi

USER root

COPY requirements.txt /usr/src/fastapi/

RUN pip install -r requirements.txt

RUN mkdir -p fastapi_example

COPY fastapi_example/ /usr/src/fastapi/fastapi_example

COPY run.sh /usr/src/fastapi/

CMD sh run.sh