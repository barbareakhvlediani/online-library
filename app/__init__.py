from flask import Flask
from app.extensions import db, migrate, login_manager  # Import login_manager
from app.config import Config
from app.user.views import user_bp
from app.admin.views import admin_bp
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)