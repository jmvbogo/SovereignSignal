from flask import Flask, request, jsonify
from src.sig_001.aletheia import analyze_claim
app = Flask(__name__)
@app.route('/api/submit_claim', methods=['POST'])
def submit():
    data = request.json
    result = analyze_claim(data)
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)