from flask import Flask
from app.ServiceContainer import ServiceContainer
import requests
class TodoService:
    def __init__(self, app: Flask, services: ServiceContainer):
        return

    def get_prioritised_tasks(self, context: str):
        url = "http://192.168.0.107:5678/webhook/getTasks"
        res = requests.post(url, json={"context": context})
        print(res)
        if res.ok:
            data = res.json()[0]['output']['recommended']
            return data
        