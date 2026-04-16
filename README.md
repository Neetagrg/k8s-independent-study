# Resilient Kubernetes-Based CI/CD Deployment
**CS Independent Study — Spring 2026**
**Neeta Misericordia | St. Johns University | Instructor: Prof. Fazel Keshtkar**

[![CI/CD Pipeline](https://github.com/Neetagrg/k8s-independent-study/actions/workflows/ci.yml/badge.svg)](https://github.com/Neetagrg/k8s-independent-study/actions/workflows/ci.yml)

---

## What This Project Is

This project builds and evaluates a resilient containerized microservice using Kubernetes and CI/CD automation. The goal is to explore how Kubernetes self-healing and auto-scaling work in practice through real experiments with measured results.

The service is a Python Flask app deployed on a local Kubernetes cluster (minikube) with:
- Automated CI/CD pipeline via GitHub Actions
- Liveness and readiness probes for self-healing
- Horizontal Pod Autoscaling (HPA) based on CPU usage
- Docker image published to Docker Hub on every push to main

**Docker Hub:** https://hub.docker.com/r/neetamis/k8s-microservice

---

## Project Structure
at > README.md << 'ENDOFREADME'
# Resilient Kubernetes-Based CI/CD Deployment
**CS Independent Study — Spring 2026**
**Neeta Misericordia | St. Johns University | Instructor: Prof. Fazel Keshtkar**

[![CI/CD Pipeline](https://github.com/Neetagrg/k8s-independent-study/actions/workflows/ci.yml/badge.svg)](https://github.com/Neetagrg/k8s-independent-study/actions/workflows/ci.yml)

---

## What This Project Is

This project builds and evaluates a resilient containerized microservice using Kubernetes and CI/CD automation. The goal is to explore how Kubernetes self-healing and auto-scaling work in practice through real experiments with measured results.

The service is a Python Flask app deployed on a local Kubernetes cluster (minikube) with:
- Automated CI/CD pipeline via GitHub Actions
- Liveness and readiness probes for self-healing
- Horizontal Pod Autoscaling (HPA) based on CPU usage
- Docker image published to Docker Hub on every push to main

**Docker Hub:** https://hub.docker.com/r/neetamis/k8s-microservice

---

## Project Structure
k8s-independent-study/
├── app.py                    # Flask microservice (5 endpoints)
├── Dockerfile                # Container build definition
├── requirements.txt          # Python dependencies
├── kubernetes/
│   ├── deployment.yaml       # 2 replicas, liveness + readiness probes
│   ├── service.yaml          # NodePort service on port 30080
│   └── hpa.yaml              # HPA: min=2, max=5 pods, 50% CPU threshold
├── .github/workflows/
│   └── ci.yml                # GitHub Actions CI/CD pipeline
├── screenshots/              # Experiment evidence screenshots
└── docs/                     # Progress reports

---

## API Endpoints

| Endpoint | Purpose | Response |
|----------|---------|----------|
| `/` | Basic service info | 200 OK |
| `/health` | Liveness probe | `{"status": "UP"}` |
| `/ready` | Readiness probe | `{"status": "READY"}` |
| `/info` | Hostname, uptime, version | 200 OK JSON |
| `/metrics` | Prometheus-format metrics | Plain text |

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- Python 3.11+
- Git

---

## Option A — Run Locally with Python

```bash
git clone https://github.com/Neetagrg/k8s-independent-study.git
cd k8s-independent-study
pip install -r requirements.txt
python app.py
curl http://localhost:5000/health
```

---

## Option B — Run with Docker

```bash
docker build -t k8s-microservice:1.0.0 .
docker run -p 5000:5000 k8s-microservice:1.0.0
curl http://localhost:5000/health
```

Or pull directly from Docker Hub:

```bash
docker run -p 5000:5000 neetamis/k8s-microservice:latest
```

---

## Option C — Deploy to Kubernetes (minikube)

```bash
minikube start
minikube addons enable metrics-server
docker build -t k8s-microservice:1.0.0 .
minikube image load k8s-microservice:1.0.0
kubectl apply -f kubernetes/
kubectl get pods
minikube service k8s-microservice
```

---

## Horizontal Pod Autoscaling

```bash
kubectl apply -f kubernetes/hpa.yaml
kubectl get hpa

# Trigger load test
kubectl run load-generator --image=busybox --restart=Never -- \
  /bin/sh -c "while true; do wget -q -O- http://k8s-microservice:5000/; done"

kubectl get hpa -w
kubectl delete pod load-generator
```

---

## CI/CD Pipeline

Every push to main triggers automatically:

1. pip install requirements.txt
2. flake8 app.py — lint check
3. docker build — build image
4. docker run + curl /health — test container
5. docker push — publish to Docker Hub (main branch only)

Secrets needed in GitHub repo settings:
- `DOCKER_HUB_USERNAME`
- `DOCKER_HUB_ACCESS_TOKEN`

---

## Experiment Results

**Self-Healing:** Deleted a pod manually — Kubernetes replaced it in **7 seconds**

**Auto-Scaling:** CPU spiked to 145% — HPA scaled from **2 to 5 pods in ~45 seconds**

---

## Progress Reports

| Phase | Weeks | Topic |
|-------|-------|-------|
| Phase 1 | 1-4 | Containerization and Kubernetes deployment |
| Phase 2 | 5-8 | CI/CD pipeline integration |
| Phase 3 | 9-11 | Self-healing and auto-scaling |
| Phase 4 | 12-14 | Monitoring with Prometheus (upcoming) |

---

*St. Johns University | CS Independent Study | Spring 2026*
