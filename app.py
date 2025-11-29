from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database configuration
DB_USER = os.getenv('DB_USER', 'default_user')
SECRET_API_KEY = os.getenv('SECRET_API_KEY', '')

@app.route('/')
def health_check():
    return jsonify({
        'status': 'ok',
        'service': 'backend-service-v2',
        'version': '2.0.1'
    }), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get list of users"""
    # TODO: Implement database query
    return jsonify({
        'users': [],
        'count': 0
    }), 200

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    # TODO: Implement database query
    return jsonify({
        'id': user_id,
        'name': 'Unknown',
        'email': 'unknown@example.com'
    }), 200

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'database': 'connected' if DB_USER else 'disconnected'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

