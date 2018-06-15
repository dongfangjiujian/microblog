from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


login = LoginManager()
login.login_view='auth.login'
db= SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)


    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')


    from .admin import admin as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')



    return app