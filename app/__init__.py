from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import required
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    config_name.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    #注册蓝本
    from .main import Blueprint as main_blueprint
    app.register_blueprint(main_blueprint)

    return app