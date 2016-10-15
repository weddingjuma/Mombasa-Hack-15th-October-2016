from flask import Flask
from flask import jsonify
from flask import request

app = Flask('voice-box')

@app.route('/api/ussd/callback', methods=['POST'])

def ussd():
    resp 
