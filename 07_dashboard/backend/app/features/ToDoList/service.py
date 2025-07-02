from flask import Flask
from app.ServiceContainer import ServiceContainer
from app.features.ToDoList.models import Directive, Initiative, Task

NOTION_TASKS_DB_ID = "NOTION_TASKS_DB_ID"
NOTION_INITIATIVES_DB_ID = "NOTION_INITIATIVES_DB_ID"
NOTION_DIRECTIVES_DB_ID = "NOTION_DIRECTIVES_DB_ID"

class TodoService:
    def __init__(self, app: Flask, services: ServiceContainer):
        self._notionClient = services.notion_client
        self._tasks_db = app.config[NOTION_TASKS_DB_ID]
        self._initiatives_db = app.config[NOTION_INITIATIVES_DB_ID]
        self._directives_db = app.config[NOTION_DIRECTIVES_DB_ID]

    def get_prioritised_tasks(self, context: str):
        directives = [Directive.from_notion_page(d) for d in self._get_active_directives()]
        initiatives = [Initiative.from_notion_page(i) for i in self._get_active_iniatives()]
        tasks = [Task.from_notion_page(t) for t in self._get_active_tasks()]

        

    # ===== Private =====

    def _get_active_tasks(self):
        db_filter = {
            "and": [
                {
                    "property": "InitiativeIsActive",
                    "rollup": {
                        "any": {
                            "checkbox": {
                                "equals": True
                            }
                        }
                    }
                },
                    {
                    "property": "DirectiveIsActive",
                    "formula": {
                        "checkbox": {
                            "equals": True
                        }
                    }
                },
                {
                    "property": "Done",
                    "checkbox": {
                        "equals": False
                    }
                }
            ]
        }
        res =  self._notionClient.query_db(self._tasks_db, db_filter)
        return res 
        
    def _get_active_iniatives(self):
        db_filter = {
            "and": [
                {
                    "property": "DirectiveIsActive",
                    "rollup": {
                        "any": {
                            "checkbox": {
                                "equals": True
                            }
                        }
                    }
                },
                {   
                    "property": "IsActive",
                    "checkbox": {
                        "equals": True
                    }
                },
                {
                    "property": "Done",
                    "checkbox": {
                        "equals": False
                    }
                }
            ]
        }
        res =  self._notionClient.query_db(self._initiatives_db, db_filter)
        return res
    
    def _get_active_directives(self):
        db_filter = {
            "and": [
                {   
                    "property": "IsActive",
                    "checkbox": {
                        "equals": True
                    }
                },
                {
                    "property": "Done",
                    "checkbox": {
                        "equals": False
                    }
                }
            ]
        }
        res =  self._notionClient.query_db(self._directives_db, db_filter)
        return res 