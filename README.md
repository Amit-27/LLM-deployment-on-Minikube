# 🚀 LLM Deployment on Kubernetes (Minikube)

## 📌 Overview

This project demonstrates how to deploy a **Large Language Model (LLM)** locally using **Kubernetes (Minikube)**. It includes containerized model serving, API exposure, and Kubernetes resource configurations to simulate a production-like environment.

The goal is to showcase **DevOps + Cloud + AI integration**, aligned with real-world **SRE and MLOps practices**.

---

## 🧠 Key Features

* Deploy LLM locally using Minikube
* Kubernetes-based architecture
* REST API for prompt-based interaction
* Scalable and containerized design
* Debugging and troubleshooting workflows
* Production-like setup with probes and services

---

## 🏗️ Architecture

```text
User (curl/API)
      │
      ▼
Kubernetes Service
      │
      ▼
LLM API Pod (Python App)
      │
      ▼
LLM Model (Ollama / Local Model)
```

---

## ⚙️ Tech Stack

* Kubernetes (Minikube)
* Docker
* Python (FastAPI)
* LLM (Ollama)
* kubectl CLI
* Git & GitHub

---

## 📂 Project Structure

```text
llm-minikube-deployment/
│
├── deployment/
│   ├── deployment.yaml
│   ├── service.yaml
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│
├── docs/
│   ├── architecture.md
│   ├── troubleshooting.md
│
├── logs/
│
└── README.md
```

---

## 🚀 Setup & Installation

### 1️⃣ Start Minikube

```bash
minikube start
```

### 2️⃣ Apply Kubernetes Configurations

```bash
kubectl apply -f deployment/
```

### 3️⃣ Verify Pods

```bash
kubectl get pods
```

### 4️⃣ Access Service

```bash
minikube service <service-name>
```

---

## 🔍 API Usage

### Example Request:

```bash
curl -X POST "http://<NODE-IP>:<PORT>/ask?prompt=Explain Kubernetes"
```

### Expected Response:

```json
{
  "response": "Kubernetes is an open-source container orchestration platform..."
}
```

---

## 🛠️ Troubleshooting

### ❌ Issue: Internal Server Error

**Possible Causes:**

* Model not loaded
* API crash inside container
* Incorrect service port mapping

**Fix:**

```bash
kubectl logs <pod-name>
kubectl describe pod <pod-name>
```

---

### ❌ Pod Not Starting

**Fix:**

```bash
kubectl get events
kubectl describe deployment <deployment-name>
```

---

## ❤️ Health Checks (Recommended Improvements)

Add liveness & readiness probes:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 10
  periodSeconds: 5

readinessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 5
```

---

## 🌐 Future Enhancements

* Add Ingress for external access
* Implement autoscaling (HPA)
* Add monitoring (Prometheus + Grafana)

---

## 📈 Learning Outcomes

* Hands-on Kubernetes deployment
* Debugging real-world production issues
* API integration with AI models
* Understanding container orchestration
* Exposure to MLOps fundamentals

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## ⭐ Acknowledgment

This project is part of hands-on learning for hosting LLM Model.

---

## 📬 Contact

If you found this useful, connect with me on GitHub and give a ⭐ to the repo!
