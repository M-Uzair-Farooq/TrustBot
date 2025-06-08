from huggingface_hub import InferenceClient
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from huggingface_hub import InferenceClient
import pyotp
import qrcode
import os
from io import BytesIO
from base64 import b64encode
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    qr_code_data = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists.')
            return redirect(url_for('register'))

        otp_secret = pyotp.random_base32()
        new_user = User(username=username,
                        password=generate_password_hash(password),
                        otp_secret=otp_secret)
        db.session.add(new_user)
        db.session.commit()

        totp_uri = pyotp.totp.TOTP(otp_secret).provisioning_uri(
            name=username, issuer_name="TrustBot")
        img = qrcode.make(totp_uri)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        qr_code_data = b64encode(buffered.getvalue()).decode("utf-8")

        flash('Scan the QR code with Google Authenticator or similar app.')
        return render_template('register.html', qr_code_data=qr_code_data)

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        otp = request.form['otp']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            totp = pyotp.TOTP(user.otp_secret)
            if totp.verify(otp):
                session['user_id'] = user.id
                session['username'] = user.username
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid 2FA code.")
        else:
            flash("Invalid credentials.")
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Login first.")
        return redirect(url_for('login'))
    return render_template('dashboard.html')


@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash("Login first.")
        return redirect(url_for('login'))
    return render_template('profile.html', username=session.get('username'))


@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for('login'))


@app.before_request
def create_tables_once():
    if not hasattr(app, 'db_initialized'):
        db.create_all()
        app.db_initialized = True


@app.route('/chat', methods=['POST'])
def chat():
    if 'user_id' not in session:
        return {"error": "Unauthorized"}, 401

    user_input = request.json.get('message')
    if not user_input:
        return {"error": "No message provided"}, 400

    try:
        hf_token = os.getenv("HF_TOKEN")
        client = InferenceClient(
            token=hf_token
        )

        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            messages=[
                {"role": "user", "content": user_input}
            ],
        )

        reply = response.choices[0].message.content
        return {"reply": reply}
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == '__main__':
    app.run(debug=True)
