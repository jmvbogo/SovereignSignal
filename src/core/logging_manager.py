"""
Manages immutable, append-only audit logs.
"""
import os
import json

class LoggingManager:
    def __init__(self, log_dir='output'):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def log(self, filename: str, entry: dict):
        path = os.path.join(self.log_dir, filename)
        with open(path, 'a') as f:
            f.write(json.dumps(entry) + '\n')
