from . import admin
from app import db
from app.models import User
from flask import redirect,url_for ,render_template

@admin.route('/index')
def index():
    user_list = User.query.all()
    return render_template('admin/index.html',title='ShowUsers',user_list=user_list)