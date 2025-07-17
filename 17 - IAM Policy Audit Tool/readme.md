# IAM Policy Audit Tool

This use case implements a Python-based audit tool to analyze IAM users, groups, and roles along with their attached policies to help identify overly permissive or unused permissions.

## Overview

The goal is to improve AWS account security by auditing IAM entities and the policies assigned to them. This helps identify:
- IAM users/roles with administrative or wildcard permissions.
- Unused IAM users or access keys.
- Inline vs managed policies.
- Roles without recent usage.

## Steps Implemented

1. **Setup and Configuration**
   - Installed and configured Boto3 and AWS credentials.
   - Ensured the user running the script had `iam:List*`, `iam:Get*`, and `iam:GenerateServiceLastAccessedDetails` permissions.

2. **Script Functionality**
   - Retrieved all IAM users, groups, and roles.
   - Collected attached policies (both managed and inline).
   - Identified entities with `AdministratorAccess` or wildcard (`*`) actions.
   - Fetched service last accessed details to detect unused permissions or inactive roles.

3. **Reporting**
   - Compiled results into a readable report.
   - Exported the audit output into CSV or Excel.
   - Optionally integrated email report distribution via SES.

## Key Concepts

- **Security Best Practices**: Principle of least privilege.
- **Policy Types**:
  - Managed policies (AWS or customer managed)
  - Inline policies
- **Access Advisor**: Used to get last accessed services for roles.

## AWS Services Used

- AWS IAM
- AWS IAM Access Analyzer (optional)
- AWS Boto3 SDK
- Amazon SES (for email reports, optional)

## Files Included

- `iam_audit.py` – Python script to perform the audit.
- `iam_audit_report.csv` – Generated audit report.
- `iam_audit_tool_documentation.pdf` – Detailed documentation of the auditing process and results.
