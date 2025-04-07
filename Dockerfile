FROM python:3.8

WORKDIR /app

#RUN apt-get update && \
#    apt-get install -y python3 python3-pip && \
#    apt-get clean 

#COPY requirements.txt .
COPY manifests/pipHello.yaml .
COPY scripts/kbf-run.py . 

RUN pip install kfp

CMD ["python","kbf-run.py"]


