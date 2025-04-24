FROM argoproj/argoexec:v3.4.10 as argoexec

FROM python:3.9

WORKDIR /app

#RUN apt-get update && \
#    apt-get install -y python3 python3-pip && \
#    apt-get clean 
COPY --from=argoexec /var/run/argo/argoexec /var/run/argo/argoexec
COPY manifests/pipHello.yaml .
COPY scripts/kbf-run.py . 

RUN pip install kfp

CMD ["python","kbf-run.py"]


