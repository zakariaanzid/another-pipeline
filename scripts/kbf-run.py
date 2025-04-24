#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os
from kfp.client import Client

#os.environ["NO_PROXY"] = "*.kubeflow,*.local"

#client = Client(host='localhost')
client = Client(host='http://ml-pipeline.kubeflow.svc.cluster.local:8888')

run = client.create_run_from_pipeline_package(
    '/app/pipHello2.10.0.yaml',
    arguments={
        'recipient': 'World',
    },
)


# In[ ]:




