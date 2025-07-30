# Encrypt S3, Set Lifecycle Rules, Monitor Logs

This use case demonstrates how to **secure an S3 bucket** using **KMS-based encryption**, configure **lifecycle rules** to optimize storage costs, and enable **access logging** for monitoring.

---

## 🧩 Use Case Overview

We implement three essential S3 features in this workflow:

1. **Encrypt S3 bucket** using AWS Key Management Service (KMS).
2. **Set a lifecycle rule** to transition objects to **S3 Glacier Instant Retrieval** after 30 days.
3. **Enable logging** by configuring a separate logging bucket to store access logs for monitoring and auditing purposes.

---

## 🛠 Services Used

- **Amazon S3**: For storing data and enabling encryption, lifecycle, and logging features.
- **AWS KMS**: For managing customer-managed keys to encrypt S3 objects.
- **(Optional)** AWS CloudTrail/CloudWatch: For extended monitoring (not covered in basic setup).

---

## ✅ Features

- **Server-Side Encryption (SSE-KMS)** for secure object storage.
- **Lifecycle Management** to automatically move infrequently accessed objects to Glacier storage class.
- **Access Logging** for audit trails and visibility into S3 operations.

---

## 🧱 Architecture

```
+-------------------------+
|     Logging Bucket      |
|  (Stores Access Logs)   |
+-----------▲-------------+
            |
+-----------|-------------+
|     Primary S3 Bucket   |
|                         |
| - SSE-KMS Encryption    |
| - Lifecycle Rule (30d)  |
| - Access Logging        |
+-------------------------+
```

---

## 🚀 Implementation Steps

1. **Create the Logging Bucket**:
   - Name: `my-s3-logs-bucket`
   - Disable public access.
   - No encryption required (optional).

2. **Create the Primary Bucket**:
   - Name: `my-secure-bucket`
   - Enable **Server-Side Encryption** with **AWS KMS key (SSE-KMS)**.
   - Disable public access.

3. **Set Lifecycle Rule**:
   - Apply to all objects.
   - Transition to **S3 Glacier Instant Retrieval** after **30 days**.

4. **Enable Logging** on Primary Bucket:
   - Set the target bucket as `my-s3-logs-bucket`.
   - Define a prefix for logs (e.g., `access-logs/`).

---

## 📂 Project Structure (if automated via IaC)

```
├── terraform/
│   ├── s3_secure_bucket.tf
│   ├── s3_logging_bucket.tf
│   ├── kms_key.tf
│   └── lifecycle_policy.tf
├── README.md
```

---

## 📌 Notes

- Make sure the logging bucket and the source bucket are in the **same region**.
- If using custom KMS keys, ensure the proper **IAM permissions** are granted to S3 for encryption/decryption.
- Lifecycle transitions may incur Glacier retrieval costs later. Use for archival data.

---

Let me know if you’d like this setup implemented via **Terraform** or **CloudFormation**.
