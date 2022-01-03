from flask import Flask, g, current_app


def create_app():
    # Flask Config
    from .config.config import Config

    app = Flask(__name__)
    app.config.from_object(Config)

    # Database Config
    from domain.models.database import mongo

    mongo.init_app(app)

    # Startup Config
    from .tools.ptcg_sdk import organized_master_set

    app.master_set = organized_master_set()

    # Register Blueprints
    from .blueprints.home_blueprint import home_views
    from .blueprints.sets_blueprint import set_views
    from .blueprints.grailed_blueprint import grailed_views

    app.register_blueprint(home_views)
    app.register_blueprint(set_views)
    app.register_blueprint(grailed_views)

    return app
