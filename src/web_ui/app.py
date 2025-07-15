"""
Veracity Chronicle - Flask Web UI for the Sovereign Signal.
"""
from flask import Flask, render_template
from .api import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/ui')

@app.route('/')
def index():
    """
    Renders the main dashboard.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
