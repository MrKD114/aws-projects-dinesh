# EC2 Instance Management – Launch and Access

This use case demonstrates how to create and manage an EC2 instance on AWS. It includes steps for launching an instance, connecting via SSH using a key pair, and configuring basic security groups.

## Objectives

- Launch an EC2 instance using the AWS Management Console
- Generate and use a key pair for SSH access
- Configure a security group to control inbound traffic
- Understand the EC2 instance lifecycle: start, stop, reboot, and terminate

## AWS Services Used

- Amazon EC2
- Amazon VPC
- EC2 Key Pairs
- Security Groups

## Steps Covered

1. Launch a new EC2 instance (Amazon Linux 2 or Ubuntu)
2. Create and download a `.pem` key pair
3. Set up a security group:
   - Allow SSH (port 22) from your IP
4. Connect to the instance using:
   ```bash
   ssh -i "your-key.pem" ec2-user@<public-ip>
