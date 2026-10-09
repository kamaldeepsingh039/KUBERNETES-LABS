# Kubernetes Hands-On Labs

This repository contains practical Kubernetes labs built while working through core container orchestration concepts.

The goal of this repo is to demonstrate hands-on understanding of Kubernetes resources, scheduling, networking, storage, security, scaling, and troubleshooting.

## What This Repository Covers

### Workloads
- Deployments
- ReplicaSets
- Pods
- StatefulSets
- Self-healing
- Rolling updates

### Networking
- ClusterIP Services
- EndpointSlices
- NGINX Ingress Controller
- Ingress routing
- NetworkPolicy basics

### Configuration
- ConfigMaps
- Environment variables
- Mounted configuration files

### Storage
- PersistentVolumeClaims
- StorageClasses
- Persistent storage testing
- StatefulSet storage persistence

### Scheduling
- nodeSelector
- Node affinity
- Pod anti-affinity
- Taints and tolerations
- Topology spread constraints

### Scaling and Reliability
- Manual replica scaling
- Horizontal Pod Autoscaler
- CPU-based scaling
- Readiness probes
- Liveness probes
- Resource requests and limits
- OOMKilled troubleshooting

### Security
- ServiceAccounts
- Roles
- RoleBindings
- Namespace-scoped RBAC
- Least-privilege permission testing

## Application

The Kubernetes manifests deploy a small Flask application packaged as a Docker container.

The application includes:

- `/` application endpoint
- `/health` health endpoint
- Docker container configuration
- PostgreSQL environment-variable support

The Kubernetes Deployment used an image hosted in Amazon ECR during the labs.

If reproducing this project, replace the image reference in the Deployment manifest with your own container registry image.

## Repository Structure

```text
KUBERNETES-LABS/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── kubernetes/
│   ├── config/
│   ├── networking/
│   ├── rbac/
│   ├── storage/
│   └── workload/
│
├── README.md
└── .gitignore
