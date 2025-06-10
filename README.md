# 🤖 TrustBot – A Secure AI Chatbot Web Application

**TrustBot** is a secure, user-friendly web application that integrates modern authentication mechanisms and AI chatbot capabilities using the Hugging Face `mistralai/Mixtral-8x7B-Instruct-v0.1` model. It combines Flask, SQLAlchemy, and PyOTP for building a full-stack intelligent system with Two-Factor Authentication (2FA) and a clean, interactive UI.

---

## 🔐 Key Features

### ✅ User Authentication
- Secure **User Registration** and **Login**
- Password hashing with Werkzeug for secure storage
- Login validations and CSRF protection

### 🔒 Two-Factor Authentication (2FA)
- PyOTP-based Time-Based One-Time Passwords
- QR Code generation using `qrcode` and `pyotp`
- Users are prompted to enter a TOTP after login

### 🤖 AI-Powered Chatbot
- Integrated with Hugging Face's `Mixtral-8x7B-Instruct-v0.1`
- Handles conversational input dynamically via AJAX
- Display chat history between user and TrustBot

### 🧠 Hugging Face Integration
- Uses `InferenceClient` for real-time responses
- Token-based secure API communication

### 📋 Dashboard
- Clean and intuitive UI using Bootstrap
- Users see welcome messages and chatbot interface after successful login

---

## 🛠️ Tech Stack

| Layer        | Technology Used                     |
|--------------|-------------------------------------|
| Backend      | Flask, SQLAlchemy                   |
| Frontend     | HTML5, Bootstrap, JavaScript (AJAX) |
| Authentication | Werkzeug, PyOTP, qrcode            |
| AI/ML        | Hugging Face `mistralai/Mixtral`    |
| Database     | SQLite (for development)            |

---

## 📁 Project Structure

```text
TrustBot/
├── 🐍 app.py                 
├── 🗃️ models.py              
├── ⚙️ config.py               
├── 🛢️ init_db.py             
│
├── 📂 templates/              # Frontend templates
│   ├── 🔑 login.html          
│   ├── ✏️ register.html       
│   └── 🖥️ dashboard.html      
│
├── 📂 static/                 # Static assets
│   └── 🎨 style.css           
│
├── 📜 requirements.txt        # Python dependencies
└── 📖 README.md               

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/TrustBot.git
   cd TrustBot
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env file**:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   HUGGINGFACE_TOKEN=your_huggingface_api_token
   ```

5. **Initialize the database**:
   ```bash
   python init_db.py
   ```

6. **Run the app**:
   ```bash
   flask run
   ```

Visit http://127.0.0.1:5000 in your browser to use TrustBot!

---

## 📌 Future Enhancements
- Dockerization for portability
- Role-based user access control
- HTTPS with Let's Encrypt
- MongoDB/PostgreSQL migration
- Integration with voice AI assistants

---

## 📧 Contact

For questions, issues, or contributions:

**Author**: M Uzai Farooq  
**Email**: m.uzair.farooq.514@gmail.com

Built with ❤️ for Secure Conversational AI!
