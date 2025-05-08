# Django PDF-to-Text API Project

This project exposes a secure API that converts PDF files stored in a local folder to text, returning the result as a JSON response. A middleware layer enforces API key authentication for access control.

---

## 🚀 Getting Started (When You Resume Work)

Follow these steps each time you return to this project:

### 1. Open Terminal and Navigate to Project Directory

```bash
cd path/to/your/project
```

---

### 2. Activate the Virtual Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

You should see `(venv)` at the start of your terminal prompt once it's active.

---

### 3. Set Environment Variables (if needed)

If you're using `python-decouple`, make sure your `.env` file is still present in the root directory with values like:

```env
API_SECRET_KEY=your-secret-key
X_API_KEY_NAME=x-api-key
DEBUG=True
```

---

### 4. Install Requirements (Only If Needed)

If you're on a new machine or reinstalled your environment:

```bash
pip install -r requirements.txt
```

---

### 5. Run Migrations (First time only or after changes)

```bash
python manage.py migrate
```

---

### 6. Start the Django Development Server

```bash
python manage.py runserver
```

Your API will be available at:  
http://127.0.0.1:8000/api/convert-pdf/

Use `curl` or Postman with the correct API key in the header:

```bash
curl -H "x-api-key: your-secret-key" http://127.0.0.1:8000/api/convert-pdf/
```

---

## 📂 Project Structure

```
project/
├── api/                # Your Django app
│   ├── views.py
│   ├── urls.py
│   └── middleware.py
├── pdfs/               # Folder containing input PDFs
│   └── output/         # JSON results saved here
├── manage.py
├── .env
├── requirements.txt
└── README.md
```