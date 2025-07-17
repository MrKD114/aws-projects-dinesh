# main.tf

# 1. AWS Provider
provider "aws" {
  region = var.region
}

# 2. VPC
resource "aws_vpc" "main_vpc" {
  cidr_block = var.vpc_cidr

  tags = {
    Name        = "MainVPC"
    Environment = "Dev"
  }
}

# 3. Subnet
resource "aws_subnet" "main_subnet" {
  vpc_id            = aws_vpc.main_vpc.id
  cidr_block        = var.subnet_cidr
  availability_zone = "ap-south-1a"

  tags = {
    Name = "MainSubnet"
  }
}

# 4. Internet Gateway
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main_vpc.id

  tags = {
    Name = "MainIGW"
  }
}

# 5. Route Table
resource "aws_route_table" "route_table" {
  vpc_id = aws_vpc.main_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "MainRouteTable"
  }
}

# 6. Associate Subnet with Route Table
resource "aws_route_table_association" "rta" {
  subnet_id      = aws_subnet.main_subnet.id
  route_table_id = aws_route_table.route_table.id
}

# 7. EC2 Instance
resource "aws_instance" "web" {
  ami                         = "ami-0a1235697f4afa8a4"
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.main_subnet.id
  associate_public_ip_address = true

  tags = {
    Name        = "WebServer"
    Environment = "Dev"
  }
}

# 8. S3 Bucket
resource "aws_s3_bucket" "iac_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = "IaCBucket"
    Environment = "Dev"
  }
}

# 9. Block Public Access to S3
resource "aws_s3_bucket_public_access_block" "block" {
  bucket = aws_s3_bucket.iac_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
