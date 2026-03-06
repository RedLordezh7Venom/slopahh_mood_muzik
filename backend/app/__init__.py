from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from app.core.database import engine, Base
from app.models.mood_history import MoodHistory # Import model to ensure it's registered

def create_app():
    # Load environment variables
    load_dotenv()

    # Ensure database tables are created
    Base.metadata.create_all(bind=engine)

    app = Flask(__name__, static_folder='../static', static_url_path='/')

    # Configure app settings
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-vibe-key-123')
    
    # Initialize extensions
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register blueprints (to be added as we build)
    # from .api import api_bp
    # app.register_blueprint(api_bp, url_prefix='/api/v1')

    @app.route('/health_check')
    def health():
        return {"status": "ok", "framework": "flask"}

    return app
