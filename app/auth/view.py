from flask import redirect,url_for,flash,render_template
from . import auth
from app.auth.form import RegisterForm,LoginForm
from flask_login import current_user,login_user
from app import db
from app.models import User

@auth.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return  redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email = email).first()
        if user is None or user.check_password(password):
            flash('Invalid Email Address or Password')
            return redirect(url_for('auth.login'))
        return redirect(url_for('main.index'))
    return render_template('auth/login.html',title = 'Login',form=form)

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
        u=User.query.filter_by(username = form.username.data).all()
        print(u)
        flash("You have registered successfully.s")
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',title='Register',form=form)