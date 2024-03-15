from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from app.auth import bp as auth_bp
from config import Config

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app = Flask(__name__)
app.config.from_object(Config)

# init core components
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'Please log in to access this page.'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
moment = Moment(app)
babel = Babel(app, locale_selector=get_locale)

from app import models, errors
