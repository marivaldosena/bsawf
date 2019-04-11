import os

DEBUG = os.environ.get('FLASK_DEBUG', True)
SERVER_NAME = os.environ.get('SERVER_NAME', 'localhost:8000')
