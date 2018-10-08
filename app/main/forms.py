from flask_wtf import Form

from wtforms import StringField,SubmitField

from wtforms.validators import required


class NameForm(Form):
    name = StringField("Please input your name",validators=[required()])
    sub = SubmitField("提交")