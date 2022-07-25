FROM python:3.10-alpine

RUN apk add build-base \
    && pip install "uvicorn[standard]"  \
    && pip install numpy \
    && apk del build-base

COPY dist/decision_service-*-py3-none-any.whl .
RUN pip install decision_service-*-py3-none-any.whl


CMD ["uvicorn", "decision_service.main:api" , "--host", "0.0.0.0"]