from flask import Flask

def create_app():
    app = Flask(__name__)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .admin import admin as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')



    return app