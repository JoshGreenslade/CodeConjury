from . import habit_tracker_bp
from .routes import register_routes
from .controller import HabitController
from .service import HabitService

def register_habits(app, services):
    service = HabitService(app, services)
    controller = HabitController(service)
    register_routes(habit_tracker_bp, controller)
    app.register_blueprint(habit_tracker_bp)