from flask import Flask
from flask import jsonify
from flask import request

app = Flask('voice-box')

@app.route('/api/voice', methods=['POST'])

def voice_api():
    resp = '<Response><Say> Welcome to SwahiliBox</Say></Response>' 
