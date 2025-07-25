
import os
from kfp.client import Client

#client = Client()

with open("/var/run/secrets/kfp/token", "r") as f:
    token = f.read().strip()

client = Client(
    host="https://kns-job-1.jxe.10.132.0.56.nip.io/pipeline",
    verify_ssl=False,
    namespace="zakaria",
    existing_token=token
)

#client = Client(host='http://ml-pipeline.kubeflow.svc.cluster.local:8888')

run = client.create_run_from_pipeline_package(
    '/app/pipHello2.10.0.yaml',
    arguments={
        'recipient': 'zakaria',
    },
)





