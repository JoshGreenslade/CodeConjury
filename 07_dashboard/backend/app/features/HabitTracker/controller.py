from flask import jsonify, Response, request
from .service import HabitService

class HabitController:
    def __init__(self, habit_service: HabitService):
        self._service = habit_service

    def get(self):
        return jsonify(self._service.get_todays_habits())
    
    def post(self):
        habit = request.get_json()['Habit']
        checked = request.get_json()['Checked']
        self._service.set_habit_completion(habit, checked)
        return Response(status=200)
