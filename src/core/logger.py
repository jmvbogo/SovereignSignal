import json, os

def log_event(filename, data):
    path = os.path.join('output', filename)
    with open(path, 'a') as f:
        f.write(json.dumps(data) + '\n')