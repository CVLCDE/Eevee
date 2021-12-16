from flask import Flask
from flask_pymongo import PyMongo
from .views import views


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret"
    app.config["MONGO_URI"] = "mongodb://localhost:27017/eevee"
    app.config["POKEMONTCG_IO_API_KEY"] = "0401cc6b-674d-4446-ad81-5294a52c8cf7"
    mongodb_client = PyMongo(app)
    db = mongodb_client.db
    app.register_blueprint(views, url_prefix="/")

    return app
