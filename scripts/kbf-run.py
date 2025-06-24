#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
from kfp.client import Client

#os.environ["NO_PROXY"] = "*.kubeflow,*.local"

client = Client()
#client = Client(host='http://ml-pipeline.kubeflow.svc.cluster.local:8888')

with open("/var/run/secrets/kubernetes.io/serviceaccount/token", "r") as f:
    token = f.read()

#client = Client(
#    host="http://ml-pipeline.kubeflow.svc.cluster.local:8888",
#    existing_token="eyJhbGciOiJSUzI1NiIsImtpZCI6IlNtY0daRlVma0FQdkNtT00weFJOZjhfZlF0OUtjMGdUVzhLU1hSNjRWTUUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzUwNzgxMTkzLCJpYXQiOjE3NTA3Nzc1OTMsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiZDVmNDRhOGEtNDU2NC00MDE3LWFiMDAtMGE1NjI0OGRhY2M4Iiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJrdWJlZmxvdyIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJwaXBlbGluZS1ydW5uZXIiLCJ1aWQiOiI5NzMxNjdmOC1mZWQ2LTQ2OWUtOTA2Mi05MmJiYjYyYjQzYTkifX0sIm5iZiI6MTc1MDc3NzU5Mywic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50Omt1YmVmbG93OnBpcGVsaW5lLXJ1bm5lciJ9.BzSpVAypBuz-LMO_z8We1scgI77eHWCp5G-a0Hg1cU4GfRMGOj_ATKZbU46B_KiyUZUiUwqToCuz2SwYBUy2r97FaF6F-3jiuRFdDcrm9bQEDRdwdYoTmPntkbXTUX0vuotDT6ZtNDp9KZGzOXtrPZj3NxnTlKgH3PojY-NYgxwozCCodjnNS_AgatgTsoKjrB8cFyVoPRIys1DJU9zIredUSV4L9UcxTqE1DOcsfyOc9gpoPW8vONsZmO2rS98dgxLldkrFccnnkljPq6xseSFKIpq8Tqoa57ERt7JE_hkb6a_64LEo5qeK4QqaoPqSYhupPrY7bYIRwOv-l53JdA"
#)

run = client.create_run_from_pipeline_package(
    '/app/pipHello2.10.0.yaml',
    arguments={
        'recipient': 'World',
    },
)


# In[ ]:




