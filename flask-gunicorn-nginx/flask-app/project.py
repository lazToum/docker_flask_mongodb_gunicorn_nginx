# -*- coding: utf-8 -*-
import os
import sys
import datetime
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '../../')))


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'db': 'flaskDb',
    'username': 'flaskUser',
    'password': 'changeMe',
    'host': 'flask-mongo',
    'port': 27017
}

SECRET_KEY = 'gfdafg$#r345fvsg&*r435fga0vvk0kvf#$#tr4fbadfbf?vfav[?>V.Vd.>vregreDxvx='
app.config['SECRET_KEY'] = SECRET_KEY
app.config['WTF_CSRF_SECRET_KEY'] = SECRET_KEY
app.debug = True
app.config['DEBUG_TB_PANELS'] = (
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_mongoengine.panels.MongoDebugPanel'
)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# workaround for auth on flask-mongoengine https://github.com/MongoEngine/flask-mongoengine/issues/259
# app.before_first_request(
    # lambda: db.connection.authenticate(app.config['MONGODB_SETTINGS'].get('username'),
                                       # app.config['MONGODB_SETTINGS'].get('password')))
from models import db
db.init_app(app)

DebugToolbarExtension(app)

from views import index
app.add_url_rule('/', view_func=index)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
