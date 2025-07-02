from flask import jsonify, Response, request
from .service import TodoService

class TodoController:
    def __init__(self, habit_service: TodoService):
        self._service = habit_service

    def get(self):
        res = self._service.get_prioritised_tasks("test")
        return jsonify(res)

    def post(self):
        raise NotImplementedError()