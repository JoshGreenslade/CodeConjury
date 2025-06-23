from flask import jsonify, Response, request
from .service import HabitService

class HabitController:
    def __init__(self, habit_service: HabitService):
        self._service = habit_service

    def get(self):
        jsonify(self._service.get_todays_habits())
    
    def post(self):
        raise NotImplementedError()
