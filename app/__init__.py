from flask import Flask
import os
import yaml
from dotenv import load_dotenv
from logger import logger  
from .routes import main as main_blueprint

# Load environment variables
load_dotenv()


class AppConfig:
    """Class to handle application configuration."""

    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from config.yaml safely."""
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, '..', 'config', 'config.yaml')

        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
        except Exception:
            config = {}

        if 'api' in config and 'key' in config['api']:
            config['api']['key'] = os.getenv('GROQ_API_KEY')

        return config


def create_app():
    """Create and configure the Flask application."""
    
    app = Flask(__name__, template_folder='templates')

    # Load configuration
    app_config = AppConfig()
    app.config.update(app_config.config)

    logger.info("Flask application starting...")

    # Register routes
    app.register_blueprint(main_blueprint)

    return app