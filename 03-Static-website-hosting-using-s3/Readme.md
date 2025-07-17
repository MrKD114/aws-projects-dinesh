# S3 Static Website Hosting

This use case demonstrates how to host a static website using Amazon S3 by configuring public access, uploading website files, and enabling S3's built-in static hosting feature.

## Overview

Amazon S3 supports hosting static websites directly from a bucket. This approach is widely used for serving HTML, CSS, JavaScript, and image files without the need for web servers or backend infrastructure.

## Steps Implemented

1. **S3 Bucket Creation**
   - Created a bucket with a globally unique name.
   - Disabled "Block all public access" during bucket setup.

2. **Static Website Hosting Configuration**
   - Enabled static website hosting under the bucket’s "Properties" tab.
   - Defined `index.html` as the index document.
   - Optionally configured `error.html` for 404 handling.

3. **File Upload**
   - Uploaded website files (`index.html`, CSS, JS).
   - Ensured correct content-type settings for each file.

4. **Bucket Policy for Public Access**
   - Applied a public read policy to allow web access to objects:
     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Sid": "PublicReadGetObject",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::your-bucket-name/*"
         }
       ]
     }
     ```

5. **Accessing the Website**
   - Used the S3 static website endpoint URL to view the hosted site.

## Notes

- File names are case-sensitive (e.g., `Index.html` ≠ `index.html`).
- HTTPS is not natively supported on S3 static websites. For HTTPS support, integrate with Amazon CloudFront.

## Files Included

- `index.html` – Main homepage
- `error.html` – Custom error page (optional)
- `s3-public-policy.json` – Sample bucket policy used for public access
- `S3_Static_Website_Hosting_Documentation.pdf` – Full step-by-step implementation reference

