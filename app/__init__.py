# -*- coding: utf-8 -*-
__version__ = '0.1'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


from datetime import timedelta

import logging

app = Flask('app')
app.config.from_pyfile('settings.py', silent=True)

logging.basicConfig(filename='moringa.log', level=logging.INFO)
logging.basicConfig(filename='moringa.bug', level=logging.DEBUG)
logging.basicConfig(filename='moringa.err', level=logging.ERROR)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/moringa'

db = SQLAlchemy(app)

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.

from api import routes
from api import voice
from api import incoming
