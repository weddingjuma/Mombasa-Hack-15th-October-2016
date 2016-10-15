#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os

from app import (app, logging, db, settings)
from flask import (make_response, request)

from models.voice import Voice
from models.member import Member


@app.route('/voice', methods=['POST'])
def voice_callback():
    isActive     = request.values.get('isActive', None)
    sessionId    = request.values.get('sessionId', None)
    callerNumber = request.values.get('callerNumber', None)

    if isActive == '1':

        callerNumber = request.values.get('callerNumber', None)
        logging.info("caller is {}".format(callerNumber))

        response = '<Response>'
        response += '<Say maxDuration="60" playBeep="false"> Hi, '
        response += 'Welcome to the Moringa school dating challenge.'

        member = Member.query.get(callerNumber)

        if member.gender.lower() == 'female':
            # find a man
            count = Member.query.filter_by(gender = 'male').count() 
            man   = random.choice(Member.query.filter_by(gender = 'male', status='Active').all())
            logging.info("{} calling -- {}".format(member.name, man))

            if count > 0:
                response += "I'll connect you in a second </Say>"
                response += '<Dial phoneNumbers="{}" ringBackTone="{}"/>'.format(man.phoneNumber, os.environ.get('sauti'))
            else:
                response += "No love for you today, for now. </Say>"
        else:
            # find a woman
            count = Member.query.filter_by(gender='female').count()
            woman = random.choice(Member.query.filter_by(gender='female', status='Active').all())
            logging.info("{} caller - {}".format(member.name, woman))

            if count > 0:
                response += "I'll connect you in a second</Say>"
                response += '<Dial phoneNumbers="{}" ringBackTone="{}"/>'.format(woman.phoneNumber, os.environ.get('sauti'))
            else:
                response += "No love for you today, for now. </Say>"

        response += '</Response>'

        voice = Voice(sessionId=sessionId, url='')
        db.session.add(voice)
        db.session.commit()

    else:
        voice = Voice.query.filter_by(sessionId = sessionId).first()
        voice.callCost = request.values.get('amount', None)

        db.session.add(voice)
        db.session.commit()
        logging.info(request.values)
        
        response = ""


    resp = make_response(response, 200)
    resp.headers['Content-Type'] = "application/xml"
    return resp
