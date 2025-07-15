"""
Configuration loader for JSON and environment variables.
"""

import json
import os
from dotenv import load_dotenv

class ConfigLoader:
    _instance = None

    def __init__(self):
        # Load environment variables from .env
        load_dotenv()
        self.config = {}
        # Load all JSON config files
        config_dir = os.getenv("CONFIG_DIR", "config")
        for fname in os.listdir(config_dir):
            if fname.endswith(".json"):
                path = os.path.join(config_dir, fname)
                try:
                    with open(path) as f:
                        key = fname.replace(".json", "")
                        self.config[key] = json.load(f)
                except Exception:
                    pass

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ConfigLoader()
        return cls._instance

    def get_config(self):
        """Return loaded configuration dictionary."""
        return self.config
