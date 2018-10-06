from . import main

from flask import render_template

@main.errorhandler(404)
def page_not_found():
    return render_template(
