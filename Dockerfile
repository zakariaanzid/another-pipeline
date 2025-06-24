FROM python:3.9

WORKDIR /app

COPY manifests/pipHello2.10.0.yaml .
COPY scripts/kbf-run.py . 
RUN pip install kfp

CMD ["python","kbf-run.py"]


