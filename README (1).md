# Flask MySQL Kubernetes Monitoring App

Simple Flask + MySQL application deployed on Kubernetes with monitoring using Prometheus and Grafana.

## Tech Stack
- Flask
- MySQL
- Docker
- Kubernetes
- Prometheus
- Grafana

## Features
- Dockerized Flask app
- MySQL integration
- Kubernetes Deployments & Services
- Kubernetes Secrets
- Pod monitoring with Grafana

## Architecture

```text
User → Flask Pod → MySQL Pod
              ↓
      Prometheus → Grafana
```

## Run

```bash
kubectl apply -f .
```

## Monitoring Query

```promql
sum(rate(container_cpu_usage_seconds_total{pod=~".*flask.*",container!="POD"}[5m])) by (pod) * 100
```
