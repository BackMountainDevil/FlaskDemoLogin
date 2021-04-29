    # -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


from app import views, commands, errors  # noqa
