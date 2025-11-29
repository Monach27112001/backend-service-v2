"""Main entry point for backend-service-v2"""

from app import app
from config import Config

if __name__ == '__main__':
    config = Config()
    print(f"Starting backend-service-v2...")
    print(f"Database user: {config.DB_USER}")
    print(f"Debug mode: {config.DEBUG}")
    
    app.run(
        debug=config.DEBUG,
        host='0.0.0.0',
        port=5000
    )

