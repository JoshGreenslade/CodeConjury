from flask import Flask
from app.ServiceContainer import ServiceContainer

NOTION_TASKS_DB_ID = "NOTION_TASKS_DB_ID"
NOTION_INITIATIVES_DB_ID = "NOTION_INITIATIVES_DB_ID"
NOTION_DIRECTIVES_DB_ID = "NOTION_DIRECTIVES_DB_ID"

class TodoService:
    def __init__(self, app: Flask, services: ServiceContainer):
        self._notionClient = services.notion_client
        self._tasks_db = app.config[NOTION_TASKS_DB_ID]
        self._initiatives_db = app.config[NOTION_INITIATIVES_DB_ID]
        self._directives_db = app.config[NOTION_DIRECTIVES_DB_ID]

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
        dto = [i.get_str('Name') for i in res]
        return dto 
        
    def _get_active_iniatives(self):
        return
    
    def _get_active_directives(self):
        return 