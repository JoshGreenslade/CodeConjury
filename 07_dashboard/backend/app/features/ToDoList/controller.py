from flask import jsonify, Response, request
from .service import TodoService

class TodoController:
    def __init__(self, habit_service: TodoService):
        self._service = habit_service

    def get_tasks(self):
        context = request.get_json()['context']
        res = self._service.get_prioritised_tasks(context)
        return jsonify(res)

    def set_completed(self):
        context = request.get_json()
        res = self._service.set_task_completion(context['task_id'], context['completed'])
        return Response(status=200)