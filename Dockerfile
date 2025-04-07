FROM python:3.8

WORKDIR /app

COPY manifests/pipHello.yaml .
COPY scripts/kbf-run.py . 

CMD["python","kbf-run.py"]


