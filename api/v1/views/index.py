#!/usr/bin/python3
"""
Creating Flask app
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def api_status():
    """
    """
    resp = {'status': "OK"}
    return jsonify(resp)