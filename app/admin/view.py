from . import admin
from app import db
from flask_login import login_required,current_user
from app.models import User

from flask import redirect,url_for ,render_template,flash

@admin.route('/')
@admin.route('/index')
@login_required
def index():
    if current_user.is_authenticated:
        user=User.query.filter_by(username=current_user.username).first()
        if user.admin==False:
            user_list = User.query.all()
            return render_template('admin/index.html',title='ShowUsers',user_list=user_list)
        else:
            flash("You don't have permision to access this page")
            return redirect(url_for('main.index'))

@admin.route('/useredit')
def user_edit():

    user_list = User.query.all()
    return render_template('admin/user_edit.html',title='ShowUsers',user_list=user_list)

@admin.route('/delete/<username>')
def delete(username):
    user  = User.query.filter_by(username=username).first()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        flash("The member has been deleted.")
        return redirect(url_for('admin.index'))
    return "Can not delete"