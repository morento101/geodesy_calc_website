from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, environ
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
DB_NAME = 'database.db'
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'fjeiwjvuhawifj'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = environ.get('MAIL_USER')
    app.config['MAIL_PASSWORD'] = environ.get('MAIL_PASS')

    db.init_app(app)
    mail.init_app(app)

    from .views import views
    from .auth import auth
    from .handlers import errors

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(errors, url_prefix="/" )

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Щоб Перейти На Цю Сторінку, Вам Потрібно Авторизуватися'
    login_manager.login_message_category = 'error'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    print('APP CREATED!!!')    

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

    
def create_mail(app):
    mail = Mail(app)
    return mail
