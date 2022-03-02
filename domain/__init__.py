from flask import Flask


def create_app():
    # Flask Config
    app = Flask(__name__)
    app.config.from_pyfile("config/config.py")

    # Startup Config
    from .tools.ptcg_sdk import organized_master_set

    app.master_set = organized_master_set()

    # Database Config
    from .config.db import mongo

    mongo.init_app(app)

    # Register Blueprints
    from .routes.home_blueprint import home_route
    from .routes.sets_blueprint import set_views
    from .routes.grailed_blueprint import grailed_views

    app.register_blueprint(home_route)
    app.register_blueprint(set_views)
    app.register_blueprint(grailed_views)

    return app
