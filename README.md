# DevSecOps Pipeline Project

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Kubernetes](https://img.shields.io/badge/kubernetes-deployed-blue)
![Security](https://img.shields.io/badge/security-OWASP-red)
![Python](https://img.shields.io/badge/python-3.10-yellow)

A full end-to-end DevSecOps pipeline I built to automate the process of building, scanning, and deploying a containerized web application using modern DevOps tools.

## What This Does

Every time I push code to GitHub, the pipeline automatically:
- Pulls the latest code
- Builds a Docker image
- Runs a security vulnerability scan (OWASP Dependency Check)
- Pushes the image to DockerHub
- Deploys it to a Kubernetes cluster running on Minikube

## Tools & Technologies

- **Jenkins** - CI/CD
devsecops-pipeline/
├── app/                  # Flask web application
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── jenkins/
│   └── Jenkinsfile       # Pipeline definition
├── k8s/
│   └── deployment.yaml   # Kubernetes manifests
└── README.md

## How to Run Locally

**Start Jenkins and Minikube:**
```bash
sudo chmod 666 /var/run/docker.sock
docker start jenkins
minikube start --driver=docker --force
```

**Fix permissions and copy kube config:**
```bash
chmod -R 777 /root/.minikube
docker exec -it -u root jenkins mkdir -p /root/.kube
kubectl config view --raw > /tmp/kube-config
docker cp /tmp/kube-config jenkins:/root/.kube/config
docker cp /root/.minikube/. jenkins:/root/.minikube/
docker exec -it -u root jenkins chmod -R 777 /root/.minikube
```

**Access Jenkins at:** `http://localhost:8080`

**Access the app at:** `http://localhost:8090`

## Author

Built by **L1bun Gaade**
