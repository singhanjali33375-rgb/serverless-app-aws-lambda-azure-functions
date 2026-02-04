# serverless-app-aws-lambda-azure-functions
This repository demonstrates serverless application development and deployment using AWS Lambda and Azure Functions. It showcases event-driven architecture, API-based execution, auto-scaling, and cloud-native monitoring without managing servers.
# Serverless Application Development & Deployment  
Using AWS Lambda and Azure Functions

## 📌 Project Overview
This project demonstrates how to design and deploy a serverless application using AWS Lambda and Azure Functions. The application follows an event-driven architecture and removes the need for server management while ensuring scalability and reliability.

## ☁️ Technologies Used
- AWS Lambda
- Amazon API Gateway
- Azure Functions
- Amazon CloudWatch
- Azure Monitor
- Python

## 🏗️ Architecture
- Client sends HTTP request
- API Gateway triggers AWS Lambda / Azure Function
- Function processes request and returns response
- Logs and metrics are captured using CloudWatch and Azure Monitor

## 📂 Project Structure
serverless-app-aws-lambda-azure-functions/
│
├── README.md
│
├── aws-lambda/
│   ├── lambda_function.py
│   └── template.yaml
│
├── azure-functio
n/
│   ├── __init__.py
│   └── function.json
│
├── api/
│   └── api-spec.yaml
│
├── monitoring/
│   └── logging-monitoring.md
│
└── sample-events/
    └── event.json
    serverless-app-aws-lambda-azure-functions/ ├── aws-lambda/ ├── azure-function/ ├── api/ ├── monitoring/ └── sample-events/
    ## 🚀 Features
- Fully serverless architecture
- Event-driven execution
- Auto-scaling without manual intervention
- Integrated logging and monitoring
- Cloud-agnostic implementation (AWS & Azure)

## 📊 Monitoring & Logging
- AWS Lambda logs via CloudWatch
- Azure Function logs via Azure Monitor
- Logs used for debugging and performance analysis

## 🎯 Use Case
This project can be used as a backend for lightweight APIs, microservices, or automation tasks where scalability and cost-efficiency are required.

## 👤 Author
Anjali Singh
