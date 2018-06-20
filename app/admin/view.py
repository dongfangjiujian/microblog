from app import admin
from flask_admin.contrib.sqlamodel import ModelView
from app import db
from app.models import User

admin.add_view(ModelView(User,db.session))