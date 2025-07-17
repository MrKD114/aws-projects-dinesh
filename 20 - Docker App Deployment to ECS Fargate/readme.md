# Docker App Deployment to ECS Fargate

This use case demonstrates how to containerize a simple application using Docker and deploy it to AWS ECS Fargate with full automation via the AWS Console.

## Overview

We deploy a containerized Python web application using the following components:
- Docker image built and pushed to Amazon ECR
- ECS Cluster and Fargate Task Definition
- Application Load Balancer for public access
- Security groups and IAM roles configured for least privilege

## Steps Implemented

1. **Dockerize the Application**
   - Created a basic Python Flask web app
   - Defined `Dockerfile` to containerize the application

2. **Push Docker Image to Amazon ECR**
   - Created a private ECR repository
   - Pushed the local Docker image to ECR using the Console upload method

3. **ECS Cluster Setup**
   - Created an ECS cluster using Fargate launch type
   - Defined task definition with container image, port mappings, and memory/CPU specs

4. **Fargate Service Deployment**
   - Deployed the service with 1 running task
   - Configured a public Application Load Balancer to route traffic to the task

5. **Networking & Security**
   - Created VPC with public subnets and attached security groups
   - Configured IAM role for ECS tasks with ECR read access

## Key Concepts

- Containerization using Docker
- ECS Fargate serverless container deployment
- Integration with ECR and Load Balancer
- IAM roles and task execution permissions

## AWS Services Used

- Amazon ECS (Fargate)
- Amazon ECR
- Elastic Load Balancing (ALB)
- AWS IAM
- Amazon VPC
- AWS CloudWatch (logs)

## Files Included

- `app.py` – Python Flask web app
- `Dockerfile` – Container definition file
- `ecs_task_definition.json` – Task configuration sample
- `docker_ecs_fargate_documentation.pdf` – Detailed documentation of all steps
