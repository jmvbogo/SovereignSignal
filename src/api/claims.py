"""
External API for claim submission.
"""
from flask import Blueprint, request, jsonify
from ..sig_001.aletheia import AletheiaNode

claims_bp = Blueprint('claims', __name__)

@claims_bp.route('/submit_claim', methods=['POST'])
def submit_claim():
    """
    Endpoint to submit a new claim for analysis.
    """
    data = request.json
    node = AletheiaNode("ALPHA-ALETHEIA-001")
    verdict = node.process_claim(data)
    return jsonify({"verdict": verdict.__dict__})
