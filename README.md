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
3. ✅ Implement CI/CD pipeline using GitHub Actions
4. ✅ Configure liveness and readiness probes
5. ⏳ Implement Horizontal Pod Autoscaling (HPA)
6. ⏳ Set up monitoring using Prometheus
7. ⏳ Conduct structured experiments

---

## 🏗️ System Architecture



┌─────────────────────────────────────────┐│         GitHub Actions (CI/CD)          ││  Build → Test → Publish → Deploy        │└─────────────────┬───────────────────────┘│▼┌─────────────────────────────────────────┐│       Docker Image Registry             ││   (Docker Hub: neetamis/k8s-microservice)│└─────────────────┬───────────────────────┘│▼┌─────────────────────────────────────────┐│      Kubernetes Cluster (minikube)      ││                                         ││  ┌─────────────┐    ┌─────────────┐   ││  │   Pod 1     │    │   Pod 2     │   ││  │  (Replica)  │    │  (Replica)  │   ││  └─────────────┘    └─────────────┘   ││           │                │           ││           └────────┬───────┘           ││                    ▼                   ││          ┌──────────────────┐          ││          │  Service (NodePort) │       ││          └──────────────────┘          │└─────────────────────────────────────────┘
---

## 📂 Project Structure

k8s-independent-study/├── .github/│   └── workflows/│       └── ci.yml              # GitHub Actions CI pipeline├── app/│   ├── app.py                  # Flask microservice│   └── requirements.txt        # Python dependencies├── kubernetes/│   ├── deployment.yaml         # K8s deployment config│   ├── service.yaml            # K8s service config│   └── hpa.yaml               # Horizontal Pod Autoscaler (Week 9-11)├── monitoring/│   └── prometheus-config.yaml  # Prometheus setup (Week 12-14)├── docs/│   ├── week-1-4-report.md     # Containerization & K8s│   ├── week-5-8-report.md     # CI/CD Pipeline│   ├── week-9-11-report.md    # Self-healing & Autoscaling│   ├── week-12-14-report.md   # Monitoring & Evaluation│   └── screenshots/├── Dockerfile                  # Container image definition├── .gitignore└── README.md                   # This file
---

## 🚀 Quick Start

### Prerequisites
- Docker Desktop
- minikube
- kubectl
- Python 3.11+

### Local Development & Deployment

```bash
# 1. Clone repository
git clone [https://github.com/Neetagrg/k8s-independent-study.git](https://github.com/Neetagrg/k8s-independent-study.git)
cd k8s-independent-study

# 2. Build Docker image locally
docker build -t k8s-microservice:latest .

# 3. Start minikube
minikube start

# 4. Deploy to Kubernetes
kubectl apply -f kubernetes/

# 5. Verify deployment
kubectl get pods
kubectl get services

# 6. Access service
minikube service k8s-microservice
📊 Progress TimelinePhaseWeeksStatusDue DateDeliverablesContainerization & K8s1-4✅ CompleteFeb 14, 2026Docker image, K8s deployment, probesCI/CD Pipeline5-8✅ CompleteMar 14, 2026GitHub Actions, automated Docker Hub pushesSelf-healing & HPA9-11⏳ PlannedApr 4, 2026Auto-scaling, recovery testsMonitoring & Evaluation12-14⏳ PlannedApr 25, 2026Prometheus, metrics, experimentsFinal Report15⏳ PlannedMay 9, 2026Technical report, presentation🔧 Technology StackApplication:Python 3.11 / Flask / GunicornContainerization:Docker (Automated via GitHub Actions)Registry: Docker Hub (neetamis/k8s-microservice)Orchestration:Kubernetes (minikube)🧪 Testing Self-HealingBash# Get pod name
kubectl get pods

# Delete a pod manually
kubectl delete pod <POD-NAME>

# Watch Kubernetes automatically recreate the pod to maintain replica count
kubectl get pods -w
📝 ReportsWeek 1-4: Containerization & KubernetesWeek 5-8: CI/CD PipelineWeek 9-11: Self-healing & Autoscaling (Coming soon)👤 AuthorNeeta MisericordiaGitHub: @NeetagrgPortfolio: neetamisericordia.comLast Updated: March 11, 2026
---

### One Last Check
Before you push this, ensure you have also created the blank file for `docs/week-5-8-report.md` so the link doesn't lead to a 404 error. 

**Would you like me to generate the content for that `week-5-8-report.md` so you can finish all your March 14 deliverables right now?**