from . import hydration_bp
from .routes import register_routes
from .controller import HydrationController
from .service import HydrationService

def register_hydration(app, services):
    service = HydrationService(app, services)
    controller = HydrationController(service)
    register_routes(hydration_bp, controller)
    app.register_blueprint(hydration_bp)