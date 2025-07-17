# Resume Parser (Mini-Project)

This mini-project demonstrates building a resume parser using Python, initially using regular expressions, and later improved using the `python-docx` library for better support with `.docx` resumes. It focuses on extracting candidate information like name, email, phone number, and skills from uploaded resumes.

## Background

Initially, a regular expression-based parser was implemented that worked only for `.txt` files. However, it failed to extract data properly from `.pdf` and `.docx` resumes. To overcome this, the use case was reimplemented using the `python-docx` library to parse `.docx` files reliably.

## Approach 1 – Regex Based Parser (Initial Attempt)

- Accepted `.txt` resume files
- Used regular expressions to extract:
  - Name
  - Email
  - Phone number
  - Skills
- **Limitations**:
  - Incompatible with `.pdf` and `.docx` formats
  - Could not handle formatting issues
  - Inconsistent results

## Approach 2 – Using `python-docx` (Final Implementation)

- Accepted `.docx` resume files
- Used the `python-docx` library to read and parse text
- Extracted structured data using:
  - String searches
  - Section markers (e.g., "Name:", "Email:")
  - Custom rules for parsing sections
- Results were more consistent and accurate compared to regex parsing

## Python Script Features

- Read `.docx` file uploaded via file input
- Extract and print/store the parsed details
- Can be extended to write output to JSON, database, or API

## Technologies Used

- Python
- `python-docx` for reading DOCX files
- Regular expressions for pattern matching
- Optional: Flask (for UI), Boto3 (for AWS integration), DynamoDB (for storage)

## Files Included

- `regex_parser.py` – Initial script using regular expressions
- `docx_parser.py` – Improved parser using `python-docx`
- `sample_resume.docx` – Test resume file
- `resume_parser_documentation.pdf` – Detailed write-up of the use case
