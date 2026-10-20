# Kubernetes Fresher Project 0

Just some fresher projects to get my hands working on Kubernetes

## Cloud-Native E-Commerce Platform on K3s with Jenkins & SonarQube

![Kubernetes](https://img.shields.io/badge/Kubernetes-K3s-326CE5?logo=kubernetes&logoColor=white)
![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-D24939?logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/Code%20Quality-SonarQube-4E9BCD?logo=sonarqube&logoColor=white)
![Platform](https://img.shields.io/badge/Architecture-ARM64%2FAArch64-FF8800)

Production-grade deployment and CI/CD lifecycle automation for a 10-tier microservices e-commerce application running on a resource-constrained ARM64 Linux VPS using K3s, Jenkins, and SonarQube.

---

## 📐 Architecture Overview

```
                                +-------------------+
                                |   GitHub Repo     |
                                +---------+---------+
                                          |
                                          v (Webhook / Polling)
                                +---------+---------+
                                |  Jenkins Pipeline |
                                +----+---------+----+
                                     |         |
                  (Quality Analysis) |         | (Automated Deployment)
                                     v         v
                     +---------------+--+   +--+--------------------+
                     | SonarQube Scanner|   |  K3s Control Plane    |
                     +------------------+   +-----------+-----------+
                                                        |
         +----------------------------------------------+------------------------------------+
         | Namespace: webapps                                                                |
         |                                                                                   |
         |  [Frontend (NodePort: 30080)] <---> [Product Catalog Service]                     |
         |              |                                                                    |
         |              +--------------------> [Cart Service] <-----> [Redis In-Memory DB]   |
         |              |                                                                    |
         |              +--------------------> [Currency / Payment / Shipping Services]     |
         +-----------------------------------------------------------------------------------+
```

---

## 🛠️ Tech Stack & Key Components

- **Container Orchestration:** K3s (Lightweight Kubernetes)
- **CI/CD Pipeline Engine:** Jenkins LTS running via Docker socket mounting
- **Static Application Security Testing (SAST):** SonarQube Community Edition
- **Infrastructure:** Oracle Cloud VPS (Ampere ARM64 / AArch64)
- **Emulation & Runtime:** QEMU binfmt emulation (`tonistiigi/binfmt`) for multi-arch OCI compatibility
