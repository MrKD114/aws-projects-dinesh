# End-to-End Microservice Deployment with Monitoring

## 📌 Use Case Overview

This project demonstrates a **serverless microservices-based order management system** built using AWS services. It includes full backend functionality using Lambda functions and integrates Step Functions for workflow orchestration, along with SNS for real-time email notifications.

---

## 🛠️ Tech Stack

- **AWS Lambda** – Core business logic for user, order, and inventory operations  
- **API Gateway** – RESTful API interface  
- **DynamoDB** – Persistent storage for Users, Orders, and Inventory  
- **AWS Step Functions** – Workflow orchestration  
- **Amazon SNS** – Email notifications on order status  
- **Postman** – API testing

---

## 🚀 Features

- Create users and orders via API Gateway  
- Email subscription for new users  
- Inventory check before order placement  
- Order processing flow managed by Step Functions  
- Real-time order status notifications via SNS  
- Monitoring and logging integrated with CloudWatch

---

## 🧩 Architecture

1. **DynamoDB Tables:**  
   - `UsersTable`  
   - `OrdersTable`  
   - `InventoryTable`  

2. **Lambda Functions:**  
   - `CreateUserFunction`  
   - `CreateOrderFunction`  
   - `CheckInventoryFunction`  
   - `UpdateOrderStatusFunction`

3. **Step Function:**  
   Orchestrates the entire order placement process:  
   `CheckInventory ➝ CreateOrder ➝ UpdateStatus ➝ TriggerEmail`

4. **SNS Topic:**  
   - Sends real-time email alerts to users on order status updates

5. **API Gateway:**  
   - Exposes HTTP endpoints for user and order operations  
   - Tested using Postman

---

## 📧 Email Notifications Flow

- Email is collected during user creation  
- The email is automatically subscribed to an SNS topic  
- When order status changes, an email is triggered via SNS

---

## 📂 Folder Structure (suggested)

```
.
├── lambdas/
│   ├── create_user.py
│   ├── create_order.py
│   ├── check_inventory.py
│   └── update_order_status.py
├── step_function/
│   └── state_machine_definition.json
├── api_gateway/
│   └── openapi_spec.yaml
├── dynamodb_tables/
│   └── table_definitions.json
├── sns/
│   └── topic_setup.md
└── README.md
```

---

## 📌 Future Enhancements

- Add user authentication (e.g., Cognito)  
- Implement retry/error handling logic in Step Functions  
- Add a UI for user and admin roles
