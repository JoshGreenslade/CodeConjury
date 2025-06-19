from flask import Flask
from dotenv import load_dotenv
from app.ServiceContainer import ServiceContainer
from app.features.hydration.bootstrap import register_hydration
from app.config import Config

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)

    services = ServiceContainer(app.config)
    register_hydration(app, services)

    return app
