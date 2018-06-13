from . import main
from flask import render_template

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html')

@main.app_errorhandler(404)
def page_not_found(e):
    return "this page is not found."
