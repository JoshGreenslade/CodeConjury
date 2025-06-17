from flask import Flask
from features.hydration import hydration_bp

def create_app(config_class='app.config.DevConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    return app

def register_blueprints(app):
    app.register_blueprint(hydration_bp)
