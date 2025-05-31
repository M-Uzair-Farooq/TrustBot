# TrustBot (🚧 Work in Progress)

**TrustBot** is a secure, AI-integrated web application built with Flask, focused on demonstrating core principles of secure software design and development.

## 🔐 Project Goals

This project aims to implement:

- **User Registration and Login** with strong password handling
- **Two-Factor Authentication (2FA)** using PyOTP
- **Secure Database Management** via SQLAlchemy
- **Chatbot Integration** using the Hugging Face Inference API (available after login)
- **Security Features** like CSRF protection, input sanitization, secure sessions, and rate limiting
- **Environment Variable Management** using `.env` for sensitive data
- **CI/CD Automation** using Jenkins for building and deploying updates from GitHub

## 📦 Technologies Used

- Flask
- SQLAlchemy
- PyOTP
- Hugging Face Inference API
- Jenkins (for CI/CD)
- Flask-WTF
- python-dotenv

## 📌 Status

This project is currently under development. More features, testing, and improvements are on the way.

## 🔧 Local Development

```bash
git clone https://github.com/M-Uzair-Farooq/TrustBot.git
cd TrustBot
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
