# PDF Text Extraction API

This project is a Django-based REST API that extracts text content from PDF files located in a local directory and returns the content as a structured JSON response. Authentication is handled using an API key mechanism.

## Features

- Accepts PDF files from a pre-defined directory (`/pdfs`)
- Extracts text using `pdfplumber`
- Returns extracted content in JSON format via an API endpoint
- Logs errors to `error.log`
- Secured with an API key system defined in a `.env` file

## Project Structure

```
project_root/
├── manage.py
├── your_django_project/
│   └── settings.py
├── your_app/
│   └── views.py
├── pdfs/                # Directory to place PDF files to be processed
├── output/              # Generated output files and JSON response will be saved here
├── .env                 # API keys and other environment variables
├── requirements.txt     # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.8+
- Virtual environment (recommended)

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://your-repo-url.git
   cd your-repo-name
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup `.env` File**

   Create a `.env` file in the project root and add:

   ```env
   API_KEY_NAME=x-api-key
   API_SECRET_KEY=your_api_secret_here
   ```

5. **Create Required Directories**

   Ensure the following directories exist:

   ```bash
   mkdir -p pdfs
   ```

6. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

7. **Run the Server**

   ```bash
   python manage.py runserver
   ```

8. **Access the API**

   - **Endpoint:** `http://localhost:8000/api/extract/`
   - **Headers:**
     ```http
     x-api-key: your_api_key_here
     ```

## Logging

- All application errors are logged to `error.log` in the project root.

## Notes

- Only files inside the `pdfs/` folder will be processed.
---
