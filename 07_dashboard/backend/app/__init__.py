from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from app.ServiceContainer import ServiceContainer
from app.features.hydration.bootstrap import register_hydration
from app.features.HabitTracker.bootstrap import register_habits
from app.config import Config

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    services = ServiceContainer(app.config)
    register_hydration(app, services)
    register_habits(app, services)

    return app
