from flask import Flask
import os

from .extensions import db
from . import blueprints


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(app.instance_path, "data.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not os.path.isdir(app.instance_path):
        os.makedirs(app.instance_path)

    for module_ in dir(blueprints):
        module_obj = getattr(blueprints, module_)
        if hasattr(module_obj, 'bp'):
            app.register_blueprint(getattr(module_obj, 'bp'))

    db.init_app(app)

    return app
