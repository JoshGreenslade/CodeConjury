from flask import request, jsonify
from .service import HydrationService

class HydrationController:
    def __init__(self, hydration_service: HydrationService):
        self._service = hydration_service

    def get(self):
        data = self._service.get_todays_hydration_level()
        return jsonify(data)
    
    def post(self):
        value = 623
        self._service.set_todays_hydration_level(value)