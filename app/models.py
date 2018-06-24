from app import db,login
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True,unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(128),index=True,unique=True)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))

    def __repr__(self):
        return '<User{}>'.format(self.username)
    def set_password(self,password):
        self.password= generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password,password)

class Role(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role{}>'.format(self.name)

class News(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(64),unique=True)
    content=db.Column(db.Text)
    hit =db.Column(db.Integer,default=0)
    time=db.Column(db.Date,default=datetime.utcnow())
    category_id=db.Column(db.Integer,db.ForeignKey('news__category.id'))

    def __repr__(self):
        return '<Role{}>'.format(self.title)

class News_Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(128),index=True,unique=True)

    news=db.relationship('News',backref='subject')

    def __repr__(self):
        return self.name

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

