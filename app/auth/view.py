from flask import redirect,url_for,flash,render_template
from . import auth
from app.auth.form import RegisterForm
from flask_login import current_user,login_user
from app import db
from app.models import User

@auth.route('/register',methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have registered successfully.s")
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',title='Register',form=form)