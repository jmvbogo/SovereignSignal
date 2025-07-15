"""
Internal API routes for Web UI.
"""
import logging
from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/status')
def status():
    """
    Returns system health and uptime.
    """
    return jsonify({"status": "operational"})
