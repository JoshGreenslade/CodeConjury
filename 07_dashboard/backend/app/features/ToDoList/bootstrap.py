from . import todo_tracker_bp 
from .routes import register_routes
from .controller import TodoController
from .service import TodoService

def register_todo(app, services):
    service = TodoService(app, services)
    controller = TodoController(service)
    register_routes(todo_tracker_bp, controller)
    app.register_blueprint(todo_tracker_bp)