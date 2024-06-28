from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate(render_as_batch=True)
login_manager = LoginManager()
admin = Admin(name='Library Admin', template_mode='bootstrap3')

login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
