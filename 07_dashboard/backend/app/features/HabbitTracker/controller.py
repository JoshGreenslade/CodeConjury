from flask import jsonify, Response, request
from .service import HabitService

class HabbitController:
    def __init__(self, habbit_service: HabitService):
        self._service = habbit_service

    def get(self):
        raise NotImplementedError()
    
    def post(self):
        raise NotImplementedError()
