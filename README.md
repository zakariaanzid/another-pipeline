# Kubeflow Hello world Pipeline

This repository contains a compiled Kubeflow Hello world pipeline and the infrastructure to deploy it automatically on a kubernetes cluster using argpcd. a Docker image and Kubernetes job.

## Structure

- `Dockerfile`: Builds a container that runs the pipeline automatically
- `scripts/kbf-run.py`: Python script that authenticates and runs the pipeline via KFP SDK
- `manifests/`: pipHello.yaml Compiled KFP v2 pipeline definition, K8s Job and Kustomize setup to launch the container# run-pipeline
- `.gitignire`: a git ignore file
- `.github/workflows`: a github actions workflow that automatically builds a docker image and pushes it toa dockerhub repo
