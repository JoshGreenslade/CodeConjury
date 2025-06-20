from flask import jsonify, Response, request
from .service import HydrationService

class HydrationController:
    def __init__(self, hydration_service: HydrationService):
        self._service = hydration_service

    def get(self):
        data = self._service.get_todays_hydration_level()
        return jsonify(data)
    
    def post(self):
        value = request.get_json()['hydration']
        self._service.set_todays_hydration_level(value)
        return Response(status=200)
