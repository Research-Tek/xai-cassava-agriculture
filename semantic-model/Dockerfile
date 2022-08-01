FROM python:3.10-alpine

RUN apk add openjdk16-jre \
    && apk add build-base \
    && pip install "uvicorn[standard]" \
    && apk del build-base

COPY dist/ontology_service-*-py3-none-any.whl .
RUN pip install "uvicorn[standard]" \
    && pip install ontology_service-*-py3-none-any.whl

CMD ["uvicorn", "ontology_service.main:api" , "--host", "0.0.0.0"]