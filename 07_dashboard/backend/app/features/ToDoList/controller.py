from flask import jsonify, Response, request
from .service import TodoService

class TodoController:
    def __init__(self, habit_service: TodoService):
        self._service = habit_service

    def get(self):
        res = self._service.get_prioritised_tasks("I'd like some variety today - I've got plenty of free time")
        return jsonify(res)

    def post(self):
        raise NotImplementedError()