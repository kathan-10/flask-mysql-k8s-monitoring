# Flask MySQL Kubernetes Monitoring App

Simple Flask + MySQL application deployed on Kubernetes with monitoring using Prometheus and Grafana.

---

## Tech Stack

- Flask
- MySQL
- Docker
- Kubernetes
- Prometheus
- Grafana

---

## Features

- Dockerized Flask application
- MySQL database integration
- Kubernetes Deployments and Services
- Kubernetes Secrets
- Pod CPU and Memory Monitoring
- Grafana dashboards for visualization
- Flask API monitoring with Prometheus

---

## Architecture

```text
User
  ↓
Flask Pod
  ↓
MySQL Pod

Prometheus → Grafana
```

---

## Kubernetes Pods

```bash
kubectl get pods
```

Example:

```text
flask-app
mysql
prometheus
grafana
alertmanager
node-exporter
```

---

## Run Project

```bash
kubectl apply -f .
```

---

## Monitoring Queries

### Flask Pod CPU Usage

```promql
sum(rate(container_cpu_usage_seconds_total{pod=~".*flask.*",container!="POD"}[5m])) by (pod) * 100
```

### MySQL Pod CPU Usage

```promql
sum(rate(container_cpu_usage_seconds_total{pod=~".*mysql.*",container!="POD"}[5m])) by (pod) * 100
```

---

## Screenshots

### Flask Pod Monitoring

![Flask CPU](screenshots/flask-cpu.png)

### MySQL Pod Monitoring

![MySQL CPU](screenshots/mysql-cpu.png)

---

## Author

Kathan Trivedi
