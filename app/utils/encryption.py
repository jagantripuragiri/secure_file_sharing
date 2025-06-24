import hashlib
import hmac
import base64
import os

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")

def generate_encrypted_url(filename):
    token = hmac.new(SECRET_KEY.encode(), filename.encode(), hashlib.sha256).digest()
    return base64.urlsafe_b64encode(token).decode()

def verify_encrypted_url(token, filename):
    expected = generate_encrypted_url(filename)
    return hmac.compare_digest(expected, token)
