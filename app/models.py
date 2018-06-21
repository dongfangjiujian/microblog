from app import db,login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash



class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True,unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(128),index=True,unique=True)
    admin = db.Column(db.Boolean,default=False,index=True)


    def __repr__(self):
        return '<User{}>'.format(self.username)
    def set_password(self,password):
        self.password= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
