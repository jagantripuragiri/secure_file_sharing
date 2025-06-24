from flask_mail import Message
from app import mail
from flask import current_app

def send_verification_email(to_email):
    msg = Message("Verify Your Email", sender=current_app.config['MAIL_USERNAME'], recipients=[to_email])
    link = f"http://127.0.0.1:5000/client/verify/{to_email}"
    msg.body = f"Click to verify your email: {link}"
    mail.send(msg)
