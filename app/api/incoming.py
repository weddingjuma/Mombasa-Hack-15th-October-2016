#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from app import (app, logging, db, settings)
from flask import (request, make_response)
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)

from models.member import Member


@app.route('/sms', methods=['POST'])
def sms():
    _from = request.values.get('from', None)
    text  = request.values.get('text', None)

    split_text = text.split('*')

    name        = split_text[0].capitalize()
    gender      = split_text[1].lower()
    age         = split_text[2]
    preference  = split_text[3].lower()

    count = Member.query.filter_by(phoneNumber = _from).count()

    if not count > 0:
        gateway = AfricasTalkingGateway(os.environ.get('username'), os.environ.get('apikey'))
        gateway.sendMessage(_from, "You have been registered for the Moringa dating session")

        if gender.lower() == 'male':
            member = Member(name=name, age=age, preference=preference, status='active', phoneNumber=_from, gender='Male')
            db.session.add(member)
            db.session.commit()
            logging.info("user added {}".format(member))

        elif gender.lower() == 'female':
            member = Member(name=name, age=age, preference=preference, status='active', phoneNumber=_from, gender='Female')
            db.session.add(member)
            db.session.commit()
            logging.info("user added {}".format(member))

    else:
        logging.info("member already exists")


    resp = make_response("OK", 200 )
    return resp
