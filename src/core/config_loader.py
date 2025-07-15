"""
Loads and caches configuration from config/ directory.
"""
import json
import os

class ConfigLoader:
    _instance = None

    @staticmethod
    def get_instance():
        if ConfigLoader._instance is None:
            ConfigLoader()
        return ConfigLoader._instance

    def __init__(self):
        if ConfigLoader._instance:
            return
        self.config = {}
        self.load_all()
        ConfigLoader._instance = self

    def load_all(self):
        base = os.path.join(os.getcwd(), 'config')
        for fname in os.listdir(base):
            if fname.endswith('.json') or fname.endswith('.template'):
                with open(os.path.join(base, fname)) as f:
                    try:
                        self.config[fname] = json.load(f)
                    except json.JSONDecodeError:
                        self.config[fname] = {}
    def get_config(self):
        return self.config
