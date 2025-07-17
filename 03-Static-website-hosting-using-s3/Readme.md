S3 Static Website Hosting
This use case demonstrates how to host a static website using Amazon S3 by configuring public access, uploading website files, and enabling S3's static website hosting feature.

Overview
Amazon S3 allows you to host static websites directly from a bucket. It supports serving HTML, CSS, JavaScript, and media files without needing any backend server.

Steps Implemented
S3 Bucket Creation
Created a bucket with a unique name. Disabled "Block all public access" to allow public web access.

Static Website Hosting Configuration
Enabled static website hosting from the Properties tab. Set index document as index.html. Optionally configured error.html.

Uploading Website Files
Uploaded index.html, CSS, JavaScript, and images. Ensured appropriate content-type for each file.

Bucket Policy for Public Access
Added the following bucket policy to allow public read access:
{
"Version": "2012-10-17",
"Statement": [
{
"Sid": "PublicReadGetObject",
"Effect": "Allow",
"Principal": "",
"Action": "s3:GetObject",
"Resource": "arn:aws:s3:::your-bucket-name/"
}
]
}

Accessing the Website
Used the S3 static website endpoint URL (provided after enabling hosting) to access the hosted site in the browser.
