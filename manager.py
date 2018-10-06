from flask import Flask,render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import required
from flask_sqlalchemy import SQLAlchemy

from config import config
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config.from_object(config)

db = SQLAlchemy(app)
db.init_app(app)
manager = Manager(app)
class NameForm(Form):
    name = StringField('name',validators=[required()])
    choose = SelectField('choose',validators=[required()])
    sub = SubmitField('None')


class users(db.Model):
    __tablename__ =  'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)


class emails(db.Model):
    __tablename__ = 'emails'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64),index=True,unique=True)

@app.route('/')
def hello_world():
    form = NameForm()
    return render_template('index.html',form=form)



@app.route('/sql')
def sql():
    return users.query.all()
if __name__ == '__main__':
    manager.run()
