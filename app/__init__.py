from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()

#This is a very important file that connects database with the app


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://./plotflixdb?driver=ODBC+Driver+17+for+SQL+Server"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'hello'

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models to register them
    from . import models

    login_manager = LoginManager() 
    login_manager.login_view = "auth.login" #someone who is not logged in should be redirected on auth.login page
    login_manager.init_app(app)

    @login_manager.user_loader # this is a function that Flask uses za ucitavanje korisnika iz baze podataka na osnovu id-ja
    def load_user(id):
        return models.User.query.get(int(id))

    return app

