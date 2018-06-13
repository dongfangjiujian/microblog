from flask import redirect,url_for
from . import auth

@auth.route('/index')
def index():

    return "auth index"