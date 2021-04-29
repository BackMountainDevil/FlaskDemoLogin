    # -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# 指定未登录时进入登陆保护的页面之后跳转的目标页面
login_manager.login_view = 'login'
login_manager.login_message = u'请先登陆'
login_manager.login_message_categoty = 'warning'

from app import views, commands, errors  # noqa
