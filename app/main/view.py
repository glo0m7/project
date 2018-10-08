from flask import request
from . import main

from .form import NameForm

@main.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = request.form