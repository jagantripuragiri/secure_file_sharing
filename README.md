# 🔐 Secure File Sharing System

This project implements a secure file-sharing backend system using **Python**, **Flask**, and **JWT-based authentication**, where:
- **Ops users** can log in and upload files (`.pptx`, `.docx`, `.xlsx`)
- **Client users** can receive and download the shared files via generated links

---

## 🚀 Tech Stack

- **Backend Framework:** Flask
- **Authentication:** JWT (Flask-JWT-Extended)
- **Database:** SQLAlchemy (SQLite by default)
- **File Handling:** Python standard `os` and `werkzeug` utilities
- **API Testing Tool:** Postman

---

## 📦 Features

### 👨‍💻 Ops User
- Login with email and password
- Upload `.pptx`, `.docx`, `.xlsx` files
- Receive a downloadable link upon successful upload

### 👥 Client User
- (Optional extension) Can login and download shared files

### 🛡 Security
- JWT token required for upload access
- Role-based route separation (e.g., `/ops/login`, `/client/login`)

---

## 📂 Folder Structure

```bash
secure_file_sharing/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── ops_routes.py
│   │   └── client_routes.py
│   └── utils/
│       ├── encryption.py
│       └── mailer.py
├── uploads/               # Uploaded files stored here
├── main.py
├── requirements.txt
└── README.md

```
---

## 🚀 Environment Setup Instructions

📁 Backend Setup (Flask)
bash

# 1. Clone the repository
```
git clone https://github.com/jagantripuragiri/secure_file_sharing.git
cd secure_file_sharing
```

# 2. Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate  # For Windows use: venv\Scripts\activate
```

# 3. Install dependencies
```
pip install -r requirements.txt
```

# 4. Set environment variables (if needed)
```
export FLASK_APP=main.py
export FLASK_ENV=development
# On Windows use: set FLASK_APP=main.py
```

# 5. Create database and folders
```
python3
>>> from app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

# 6. Run the application
```
python3 main.py
```
```
The server will run at: http://127.0.0.1:5000
```

# 📮 API Usage (Postman)
 ## 🔑 1. Login (Ops)

```POST /ops/login
Body (JSON):

{
  "email": "ops@example.com",
  "password": "admin123"
}
```
Returns a JWT access_token.

## 📤 2. Upload File
```
POST /ops/upload
Headers:

Authorization: Bearer <access_token>

Body (form-data):

file: (choose a .pptx, .docx, or .xlsx)

```

Returns:
```
{
  "msg": "File uploaded successfully",
  "download_link": "http://127.0.0.1:5000/download/filename.pptx"
}
```
# ✅ Valid File Types
Only the following are allowed:
```
.pptx

.docx

.xlsx
```
# 👤 Default User (for testing)
You can add a test user like this via shell:
```
from app import db
from app.models import User
from werkzeug.security import generate_password_hash

user = User(email="ops@example.com", password=generate_password_hash("admin123"), role="ops")
db.session.add(user)
db.session.commit()
```

# 📌 Notes

```

Make sure to pass subject as a string field in form-data.

Uploaded files are stored in the uploads/ directory.

This is a local setup. If deploying, consider using S3, PostgreSQL, HTTPS, etc.
```

# 📧 Contact
For any issues, contact: tripuragirijagan27@example.com


