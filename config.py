import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-super-secret-key-that-is-long-and-random'
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY') or 'AIzaSyBCBqhxQ3GMqMyipPWHWFN6KbCkZA0ly6s'
    
    # Database configuration - Railway friendly
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Railway provides postgres:// but SQLAlchemy needs postgresql://
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        # Fallback to SQLite for local development
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True
    }
    
    # Production settings
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'