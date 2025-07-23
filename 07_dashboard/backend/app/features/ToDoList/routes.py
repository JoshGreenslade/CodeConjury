from .controller import TodoController

def register_routes(bp, controller: TodoController):
    bp.add_url_rule("/", view_func=controller.get_tasks, methods=["POST"])
    bp.add_url_rule("/toggle", view_func=controller.set_completed, methods=["POST"])
    bp.add_url_rule("/new", view_func=controller.add_new, methods=["POST"])