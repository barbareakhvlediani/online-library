from flask import Flask

from dotenv import load_dotenv
from app.config import Config
from app.extensions import db, migrate, login_manager

from app.user.views import user_bp
from app.admin.views import admin_bp
from app.main.views import main_bp
from app.models import User

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='app/templates')
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'



    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(main_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    # with app.app_context():
    #     print('createing database')
    #     db.create_all()
    #     print('created database')
    app.run(debug=True)
