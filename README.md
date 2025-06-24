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
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── ops_routes.py
│   │   └── client_routes.py
├── uploads/
│   └── # Uploaded files stored here
├── main.py
├── requirements.txt
└── README.md
