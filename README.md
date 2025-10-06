# Coworking Analytics - AWS EKS Project

## Project Overview
Complete AWS EKS deployment with Flask application, PostgreSQL database, Docker containerization, ECR, CodeBuild, and CloudWatch monitoring.

## Architecture
- **AWS EKS**: Kubernetes cluster hosting the application
- **PostgreSQL**: Database deployed as Kubernetes pods
- **Flask App**: Analytics service with REST APIs
- **Amazon ECR**: Container registry for Docker images
- **AWS CodeBuild**: CI/CD pipeline triggered by GitHub
- **CloudWatch**: Logging and monitoring

## API Endpoints
- `GET /health_check` - Health check endpoint
- `GET /readiness_check` - Readiness check endpoint
- `GET /api/reports/user_visits` - User visits analytics
- `GET /api/reports/daily_usage` - Daily usage statistics

## Features
- ✅ Docker containerization with security best practices
- ✅ ECR repository for image storage
- ✅ CodeBuild CI/CD pipeline with GitHub integration
- ✅ EKS cluster with managed node groups
- ✅ PostgreSQL database with sample data
- ✅ Kubernetes ConfigMaps and Secrets
- ✅ CloudWatch Container Insights monitoring
- ✅ Periodic application logging
- ✅ Health and readiness checks
- ✅ LoadBalancer service for external access

## Setup Instructions

### 1. EKS Cluster Creation
```bash
eksctl create cluster --name coworking-cluster --region us-east-1 --nodegroup-name coworking-nodes --node-type t3.small --nodes 1 --nodes-min 1 --nodes-max 2 --managed
```

### 2. Database Deployment
```bash
kubectl apply -f deployment/postgresql-deployment.yaml
kubectl apply -f deployment/postgresql-service.yaml
```

### 3. Application Configuration
```bash
kubectl apply -f deployment/configmap.yml
kubectl apply -f deployment/secrets.yml
```

### 4. Application Deployment
```bash
kubectl apply -f deployment/deployment.yaml
```

## Testing
```bash
# Get external IP
kubectl get svc coworking-service

# Test endpoints
curl http://<EXTERNAL-IP>:5153/health_check
curl http://<EXTERNAL-IP>:5153/api/reports/user_visits
curl http://<EXTERNAL-IP>:5153/api/reports/daily_usage
```

## Monitoring
- CloudWatch Container Insights enabled
- Application logs available in CloudWatch
- EKS cluster logs configured
- Periodic logging every 30 seconds

## Project Structure
```
├── analytics/           # Flask application code
├── db/                 # Database SQL scripts
├── deployment/         # Kubernetes manifests
├── Dockerfile          # Container definition
├── buildspec.yaml      # CodeBuild configuration
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

This project demonstrates a complete cloud-native application deployment using AWS best practices and modern DevOps tools.