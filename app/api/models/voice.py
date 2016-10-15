import os
import sys

from app import db


class Voice(db.Model):
    __tablename__ = 'voice'

    sessionId = db.Column(db.String(250), primary_key = True)
    url       = db.Column(db.String(250), nullable = False)
    callCost  = db.Column(db.Numeric(10), nullable = True)
    stt       = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return '<ID %r>' % self.sessionId
