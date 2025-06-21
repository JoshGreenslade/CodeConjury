from . import habbit_tracker_bp
from .routes import register_routes
from .controller import HabitController
from .service import HabitService

def register_hydration(app, services):
    service = HabitService(app, services)
    controller = HabitController(service)
    register_routes(habit_tracker_bp, controller)
    app.register_blueprint(habbit_tracker_bp)