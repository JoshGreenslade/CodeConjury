from .controller import HydrationController

def register_routes(bp, controller: HydrationController):
    bp.add_url_rule("/today", view_func=controller.get, methods=["GET"])
    bp.add_url_rule("/today", view_func=controller.post, methods=["POST"])