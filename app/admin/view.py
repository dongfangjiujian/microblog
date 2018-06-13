from . import admin
from flask import redirect,url_for

@admin.route('/index')
def index():
    return "admin index"