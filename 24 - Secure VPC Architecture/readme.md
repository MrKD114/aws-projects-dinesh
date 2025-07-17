# Secure VPC Architecture

This use case demonstrates how to build a secure Virtual Private Cloud (VPC) architecture in AWS that separates public and private resources while ensuring controlled access and internet connectivity.

## Objective

Design and deploy a secure VPC setup with properly segmented public and private subnets, NAT Gateway, route tables, security groups, and network ACLs.

## What Was Done

- Created a custom VPC with a defined CIDR block
- Created two public and two private subnets in different availability zones
- Attached an Internet Gateway to the VPC
- Created a NAT Gateway in a public subnet for private subnet internet access
- Set up route tables for public and private subnets
- Launched EC2 instances in both public and private subnets
- Configured Security Groups and Network ACLs to control traffic

## Key Components

- **VPC**: Custom VPC for isolation
- **Subnets**:
  - Public Subnet: For internet-facing resources
  - Private Subnet: For internal resources with no direct internet access
- **Internet Gateway**: For internet access to public subnet resources
- **NAT Gateway**: For outbound internet access from private subnets
- **Route Tables**:
  - Public Route Table with route to Internet Gateway
  - Private Route Table with route to NAT Gateway
- **Security Groups**: Instance-level firewall rules
- **Network ACLs**: Subnet-level traffic control

## Security Best Practices

- Only required ports opened in Security Groups (e.g., 22, 80, 443)
- Private instances have no public IP
- NACLs configured to restrict unwanted IP ranges
- Instances in private subnets access the internet through NAT Gateway

## Benefits

- Segregation of public-facing and internal components
- Better security with least privilege networking
- Scalable architecture ready for multi-tier applications

## Notes

- Can be extended to include Bastion Host for SSH access to private EC2
- Suitable base for secure, production-grade infrastructure
