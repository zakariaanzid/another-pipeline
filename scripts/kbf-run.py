#!/usr/bin/env python
# coding: utf-8

# In[1]:


from kfp.client import Client

#client = Client(host='localhost')
client = Client()

run = client.create_run_from_pipeline_package(
    '/app/manifests/pipHello.yaml',
    arguments={
        'recipient': 'World',
    },
)


# In[ ]:




