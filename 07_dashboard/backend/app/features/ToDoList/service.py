from flask import Flask
from app.ServiceContainer import ServiceContainer
import requests

from app.features.ToDoList.dtos.getPriortisedTasksDto import getPrioritisedTasksDto

TASK_DONE_KEY = "Done"

class TodoService:
    def __init__(self, app: Flask, services: ServiceContainer):
        self._notionClient = services.notion_client
        self._notion_tasks_db = app.config["NOTION_TASKS_DB_ID"]

    def get_prioritised_tasks(self, context: str):
        url = "http://192.168.0.107:5678/webhook/getTasks"
        res = requests.post(url, json={"context": context})
        print(res)
        if res.ok:
            data = res.json()[0]['output']
            return getPrioritisedTasksDto(data)
        
    def set_task_completion(self, task_id: str, completed: bool):
        self._notionClient.set_page_property(task_id, {
            TASK_DONE_KEY : {"checkbox": completed}
        })

    def add_new_task(self, task: str):
        url = "http://192.168.0.107:5678/webhook/addTask"
        res = requests.post(url, json={"Task": task})
        print(res)
        if res.ok:
            return

    # ===== Private =====
    def _get_tasks(self):
        return self._notionClient.query_db(self._notion_tasks_db)