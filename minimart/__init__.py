import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object('minimart.default_settings')
app.config.from_envvar('MINIMART_SETTINGS')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "db.sqlite3")}'
db = SQLAlchemy(app)
ma = Marshmallow(app)


if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(os.path.join(
        app.config['LOG_DIR'], 'minimart.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(
        '<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)
    
import minimart.models
import minimart.views
