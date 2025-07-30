# UC-26: Order Workflow using AWS Step Functions

This project demonstrates how to build a **Step Function-based Order Workflow** using AWS Lambda and Step Functions. It helps in understanding how state machines can orchestrate multiple services in a serverless environment.

---

## 🧩 Use Case Overview

We create a **Step Function state machine** to manage the order lifecycle. The workflow includes the following four stages:

1. **Validate Order** – Checks whether the order is valid (e.g., product availability, user data).
2. **Process Payment** – Simulates a payment step using a Lambda function.
3. **Ship Order** – Initiates a mock shipping process.
4. **Notify Customer** – Sends a notification (e.g., email/SNS) once the order is confirmed and shipped.

Each stage is implemented as a separate Lambda function. These functions are coordinated through an AWS Step Functions state machine.

---

## 🛠 Services Used

- **AWS Step Functions**: Manages and sequences the order workflow.
- **AWS Lambda**: Individual functions to perform each workflow stage.
- **(Optional)** Amazon SNS: Used for customer notifications.

---

## ✅ Features

- Modular Lambda functions per workflow stage.
- Visual representation of state transitions using Step Functions.
- Easy extension of stages (e.g., add logging, inventory checks, fraud detection).
- Cost-efficient as compute runs only during execution.

---

## 🧱 Architecture

```
        Start Execution
             |
     ┌───────▼────────┐
     │ Validate Order │
     └───────┬────────┘
             ▼
     ┌───────▼────────┐
     │ Process Payment│
     └───────┬────────┘
             ▼
     ┌───────▼───────┐
     │  Ship Order   │
     └───────┬───────┘
             ▼
     ┌───────▼─────────┐
     │ Notify Customer │
     └───────┬─────────┘
             ▼
            End
```

---

## 🚀 Deployment Steps

> Ensure you have the AWS CLI and necessary IAM permissions configured before proceeding.

1. **Create four Lambda functions**:
   - `ValidateOrderFunction`
   - `ProcessPaymentFunction`
   - `ShipOrderFunction`
   - `NotifyCustomerFunction`

2. **Define a Step Function state machine** using either the AWS Console or JSON/YAML definition:
   - Each state maps to a Lambda function invocation.

3. **Grant permissions**:
   - Step Function needs permission to invoke the Lambda functions.
   - Lambdas may need permission to publish to SNS (for notifications).

4. **Test the workflow**:
   - Manually trigger the Step Function via console or API.
   - Watch execution flow and logs.

---

## 🧪 Sample Input (for Step Function execution)

```json
{
  "orderId": "12345",
  "customerEmail": "test@example.com",
  "items": [
    { "sku": "SKU001", "quantity": 2 }
  ],
  "paymentMethod": "CreditCard"
}
```

---

## 📂 Project Structure

```
├── lambdas/
│   ├── validate_order.py
│   ├── process_payment.py
│   ├── ship_order.py
│   └── notify_customer.py
├── state_machine/
│   └── order_workflow_definition.json
├── README.md
```

---

## 📌 Notes

- This use case is ideal for beginners trying to understand **how AWS Step Functions orchestrate serverless workflows**.
- Real-world implementations can integrate **DynamoDB**, **SNS**, or **SQS** for extended functionality.

---

Let me know if you'd like this converted into a deployable Terraform/CDK/CloudFormation setup.
