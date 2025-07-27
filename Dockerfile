FROM python:3.12-alpine3.21
LABEL maintainer="Fouda Aime Emmanuel Kalvin"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.prod.txt /rmv/requirements.prod.txt
COPY ./requirements.dev.txt /rmv/requirements.dev.txt
COPY ./devlab /devlab
WORKDIR /devlab

EXPOSE 8000

ARG PROD=false

RUN python -m venv /env && \
    /env/bin/pip install --upgrade pip && \
    if [ "$PROD" = "true" ]; then \
    /env/bin/pip install -r /rmv/requirements.prod.txt; \
    fi && \
    /env/bin/pip install -r /rmv/requirements.dev.txt && \
    rm -rf /rmv && \
    adduser -D -H USER 

ENV PATH="/env/bin:${PATH}"

USER USER
    
    
