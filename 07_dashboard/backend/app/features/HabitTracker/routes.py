from .controller import HabitController

def register_routes(bp, controller: HabitController):
    bp.add_url_rule("/", view_func=controller.get, methods=["GET"])
    bp.add_url_rule("/", view_func=controller.post, methods=["POST"])