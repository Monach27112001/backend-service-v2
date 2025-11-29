"""Configuration module for backend-service-v2"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    DB_USER = os.getenv('DB_USER', 'default_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'appdb')
    
    SECRET_API_KEY = os.getenv('SECRET_API_KEY', '')
    
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False

