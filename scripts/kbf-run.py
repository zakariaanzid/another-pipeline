#!/usr/bin/env python
# coding: utf-8

# In[1]:

#import os
#from kfp.client import Client

#os.environ["NO_PROXY"] = "*.kubeflow,*.local"

#client = Client()

#with open("/var/run/secrets/kfp/token", "r") as f:
#    token = f.read().strip()

#client = Client(
#    host="https://kns-job-13.jxe.10.132.0.56.nip.io/pipeline",
#    ssl_ca_cert=False,
#    existing_token=token
#)

#client = Client(host='http://ml-pipeline.kubeflow.svc.cluster.local:8888')

#with open("/var/run/secrets/kubernetes.io/serviceaccount/token", "r") as f:
#     token = f.read()

#client = Client(
#   host="http://ml-pipeline.kubeflow.svc.cluster.local:8888",
#   existing_token=token
#)


#cliens = Client(
 #  host="http://ml-pipeline.kubeflow.svc.cluster.local:8888",
  # existing_token="yJhbGciOiJSUzI1NiIsImtpZCI6IlNtY0daRlVma0FQdkNtT00weFJOZjhfZlF0OUtjMGdUVzhLU1hSNjRWTUUifQ.eyJhdWQiOlsicGlwZWxpbmVzLmt1YmVmbG93Lm9yZyJdLCJleHAiOjE3NTA4MzkxMjgsImlhdCI6MTc1MDgzODUyOCwiaXNzIjoiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiLCJqdGkiOiIyNTY3ZmFhNy1mMGFjLTRmMzctYmIwMS00MDJmZGYwZGRjZjUiLCJrdWJlcm5ldGVzLmlvIjp7Im5hbWVzcGFjZSI6Imt1YmVmbG93Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6InBpcGVsaW5lLXJ1bm5lciIsInVpZCI6Ijk3MzE2N2Y4LWZlZDYtNDY5ZS05MDYyLTkyYmJiNjJiNDNhOSJ9fSwibmJmIjoxNzUwODM4NTI4LCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZWZsb3c6cGlwZWxpbmUtcnVubmVyIn0.nsEKakFmbPggOamVtXucTsOkzjQsvp8v_Qr1ETe_J90BD3yq3asI9H-rqMzyeOZ7TA0urIWAxyRGydGPFtc9xCUAfPeQb69akg7_V9Kv1OtnhJKvGVn_4-8c8g_l7b8AaagM15Nf9pomzp4WAajSM4-sd_QJNnL07Z3zwUAw2nGHEGUPh4uEL8p2R_TPLOtE8Fdv23C8O1R6FNimufkBkBH9yIHzfLbZitE-4GuglV-H8z1BdKe3E_H3SV17xHnX_NriOnr5TUYsGfQqE8LX4gZA2S3glUm3mIIRRV6cUX9UTJPDTo1oIBeHOVuAQ0ZWXEjNbR3kYe14EY0UTcSeUg",
   #other_headers={
    #    "x-goog-authenticated-user-email": "teamzakmaster1@test.com"
     #      }
   #)

import os
from kfp import Client
from kfp_server_api.configuration import Configuration

# Read token from mounted file
token_path = os.environ.get("KFP_AUTH_TOKEN_PATH", "/var/run/secrets/kfp/token")
with open(token_path, "r") as f:
    token = f.read().strip()

# Configure the API client
host = os.environ.get("KFP_ENDPOINT", "https://kns-job-13.jxe.10.132.0.56.nip.io/pipeline")
config = Configuration(host=host)
config.api_key = {"authorization": f"Bearer {token}"}
config.verify_ssl = False  # If you're using a self-signed cert (as in your case)

# Create the KFP client
client = Client(host=host, existing_config=config)


run = client.create_run_from_pipeline_package(
    '/app/pipHello2.10.0.yaml',
    arguments={
        'recipient': 'World',
    },
)


# In[ ]:




