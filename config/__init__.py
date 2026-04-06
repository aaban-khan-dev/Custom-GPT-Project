import os
import yaml
from dotenv import load_dotenv

class AppConfig:
    def __init__(self):
        load_dotenv()
        self.config = self.load_config()

    def load_config(self):

        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir,'..','config.yaml')

        with open(config_path,'r') as f:
            config = yaml.safe_load(f)

        if not config:
            raise ValueError("Configuration file is empty or not found.")
        
        if 'api' in config and 'key' in config['api']:
            api_key = os.getenv('GROQ_API_KEY')

            if not api_key:
                raise ValueError("API key not found in environment variables.")
        
            config['api']['key'] = api_key
        
        return config
    

config = AppConfig().config

