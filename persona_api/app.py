from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from .db import db, init_db
from .utils import import_json
from . import api


def create_app(import_name=__name__, settings_override=None):
    from .environment import SECRET_KEY, DB_URI

    settings = dict(SECRET_KEY=SECRET_KEY,
                    SQLALCHEMY_DATABASE_URI=DB_URI,
                    SQLALCHEMY_TRACK_MODIFICATIONS=False)
    if settings_override:
        settings.update(**settings_override)

    # create and configure the app
    app = Flask(import_name)
    app.config.from_mapping(**settings)

    # init app with database
    db.init_app(app)

    # register cli commands
    init_db.register_command(app)
    import_json.register_command(app)

    # register swagger blueprint
    swagger_path = '/swagger'
    swagger_config_url = '/static/swagger.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        swagger_path,
        swagger_config_url,
        config={
            'app_name': 'persona_api'
        }
    )
    app.register_blueprint(swaggerui_blueprint)

    # register api routes
    app.register_blueprint(api.blueprint)

    return app
