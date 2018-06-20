from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

login = LoginManager()
login.login_view='auth.login'
db= SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
admin=Admin(name="houtai")





def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    admin.init_app(app)





    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')


    # from .admin import admin as admin_bp
    # app.register_blueprint(admin_bp)




    return app



from app import models, admin_view
