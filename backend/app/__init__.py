# __init__.py
from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.extensions import db
from flask_migrate import Migrate
from app import models
from .apis import api

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a random secret key
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    api.init_app(app)
    db.init_app(app)
    # migrate = Migrate(app, db)
    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)
    migrate = Migrate()
    migrate.init_app(app, db, render_as_batch=True)   # render_as_batch=True this is just a workaround the limitation of sqllite - check notes
    
    with app.app_context():
        db.create_all()  # Create tables for our models

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=3000)  # Specify the port number here