"""Utility functions for backend-service-v2"""

import hashlib
import secrets

def generate_api_token():
    """Generate a random API token"""
    return secrets.token_urlsafe(32)

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    """Basic email validation"""
    if '@' not in email:
        return False
    if '.' not in email.split('@')[1]:
        return False
    return True

def sanitize_input(user_input):
    """Sanitize user input"""
    # Basic sanitization
    return user_input.strip().replace('<', '&lt;').replace('>', '&gt;')

