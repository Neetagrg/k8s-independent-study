[![CI/CD Pipeline](https://github.com/Neetagrg/k8s-independent-study/actions/workflows/ci.yml/badge.svg)](https://github.com/Neetagrg/k8s-independent-study/actions/workflows/ci.yml)

# Kubernetes Independent Study Project

**Resilient Kubernetes-Based CI/CD Deployment**

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

## 📋 Project Overview

Independent study project for Spring 2026 focusing on designing and implementing a resilient containerized microservice deployment using Kubernetes and CI/CD automation.

**Student:** Neeta Misericordia  
**Institution:** St. John's University  
**Semester:** Spring 2026  
**Duration:** January - May 2026

---

## 🎯 Project Objectives

1. ✅ Containerize a backend microservice using Docker
2. ✅ Deploy service on local Kubernetes cluster (minikube)
3. 🔄 Implement CI pipeline using GitHub Actions (In Progress)
4. ✅ Configure liveness and readiness probes
5. ⏳ Implement Horizontal Pod Autoscaling (HPA)
6. ⏳ Set up monitoring using Prometheus
7. ⏳ Conduct structured experiments

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────┐
│         GitHub Actions (CI/CD)          │
│  Build → Test → Publish → Deploy        │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│       Docker Image Registry             │
│     (Docker Hub / GitHub Packages)      │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│      Kubernetes Cluster (minikube)      │
│                                         │
│  ┌─────────────┐    ┌─────────────┐   │
│  │   Pod 1     │    │   Pod 2     │   │
│  │  (Replica)  │    │  (Replica)  │   │
│  └─────────────┘    └─────────────┘   │
│           │                │           │
│           └────────┬───────┘           │
│                    ▼                   │
│          ┌──────────────────┐          │
│          │  Service (NodePort) │       │
│          └──────────────────┘          │
└─────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
k8s-independent-study/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── app/
│   ├── app.py                  # Flask microservice
│   └── requirements.txt        # Python dependencies
├── kubernetes/
│   ├── deployment.yaml         # K8s deployment config
│   ├── service.yaml            # K8s service config
│   └── hpa.yaml               # Horizontal Pod Autoscaler (Week 9-11)
├── monitoring/
│   └── prometheus-config.yaml  # Prometheus setup (Week 12-14)
├── docs/
│   ├── week-1-4-report.md     # Containerization & K8s
│   ├── week-5-8-report.md     # CI/CD Pipeline
│   ├── week-9-11-report.md    # Self-healing & Autoscaling
│   ├── week-12-14-report.md   # Monitoring & Evaluation
│   └── screenshots/
├── Dockerfile                  # Container image definition
├── .gitignore
└── README.md                   # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Docker Desktop
- minikube
- kubectl
- Python 3.11+

### Local Development

```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/k8s-independent-study.git
cd k8s-independent-study

# Build Docker image
docker build -t k8s-microservice:1.0.0 .

# Start minikube
minikube start

# Load image into minikube
minikube image load k8s-microservice:1.0.0

# Deploy to Kubernetes
kubectl apply -f kubernetes/

# Verify deployment
kubectl get pods
kubectl get services

# Access service
minikube service k8s-microservice
```

---

## 📊 Progress Timeline

| Phase | Weeks | Status | Due Date | Deliverables |
|-------|-------|--------|----------|--------------|
| **Containerization & K8s** | 1-4 | ✅ Complete | Feb 14, 2026 | Docker image, K8s deployment, probes |
| **CI/CD Pipeline** | 5-8 | 🔄 In Progress | Mar 14, 2026 | GitHub Actions, automated builds |
| **Self-healing & HPA** | 9-11 | ⏳ Planned | Apr 4, 2026 | Auto-scaling, recovery tests |
| **Monitoring & Evaluation** | 12-14 | ⏳ Planned | Apr 25, 2026 | Prometheus, metrics, experiments |
| **Final Report** | 15 | ⏳ Planned | May 9, 2026 | Technical report, presentation |

---

## 🔧 Technology Stack

**Application:**
- Python 3.11
- Flask 3.0
- Gunicorn

**Containerization:**
- Docker
- Multi-stage builds

**Orchestration:**
- Kubernetes
- minikube (local cluster)

**CI/CD:**
- GitHub Actions
- Docker Hub / GitHub Packages

**Monitoring:**
- Prometheus
- Grafana (optional)

---

## 📖 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/health` | GET | Liveness probe |
| `/ready` | GET | Readiness probe |
| `/info` | GET | Service information |
| `/metrics` | GET | Prometheus metrics |

---

## 🧪 Testing Self-Healing

```bash
# Get pod name
kubectl get pods

# Delete a pod
kubectl delete pod <POD-NAME>

# Watch automatic recreation
kubectl get pods -w
```

Kubernetes will automatically:
1. Detect pod deletion
2. Schedule new pod
3. Maintain desired replica count (2)

---

## 📈 Monitoring

### View Logs
```bash
kubectl logs <POD-NAME>
```

### Check Pod Health
```bash
kubectl describe pod <POD-NAME>
```

### View Events
```bash
kubectl get events --sort-by='.lastTimestamp'
```

---

## 📝 Reports

Progress reports for each phase are available in `/docs`:

- [Week 1-4: Containerization & Kubernetes](docs/week-1-4-report.md)
- [Week 5-8: CI/CD Pipeline](docs/week-5-8-report.md) *(Coming soon)*
- [Week 9-11: Self-healing & Autoscaling](docs/week-9-11-report.md) *(Coming soon)*
- [Week 12-14: Monitoring & Evaluation](docs/week-12-14-report.md) *(Coming soon)*

---

## 🤝 Contributing

This is an academic project for independent study. Not accepting external contributions.

---

## 📄 License

This project is for educational purposes only.

---

## 👤 Author

**Neeta Misericordia**
- GitHub: [@Neetagrg](https://github.com/Neetagrg)
- Portfolio:(https://neetamisericordia.com)

---

## 📚 References

- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Prometheus Documentation](https://prometheus.io/docs/)

---

**Last Updated:** February 23, 2026
