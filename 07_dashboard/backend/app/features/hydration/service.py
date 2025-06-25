from flask import Flask
from app.common.notion.notion_client import NotionClient
from app.ServiceContainer import ServiceContainer
from datetime import date
from .dtos.getHydration import getHydrationDto

class HydrationService:
    def __init__(self, app: Flask, services: ServiceContainer):
        self._notionClient = services.notion_client
        self._hydration_db = app.config["NOTION_HYDRATION_DB_ID"]

    def get_todays_hydration_level(self):
        db_filter = {
            "property": "Date",
            "date": {"equals":date.today().isoformat()}
        }
        res = self._notionClient.query_db(self._hydration_db, db_filter)
        print(res)
        if not res:
            self._create_hydration_entry_for_today()
            return 0
        hydration = res[0].get_number('Amount (ml)')
        dto = getHydrationDto(hydration)
        return dto

    def set_todays_hydration_level(self, value):
        print(value)
        db_filter = {
            "property": "Date",
            "date": {"equals": date.today().isoformat()}
            }
        res = self._notionClient.query_db(self._hydration_db, db_filter)

        # If we can't find todays page, create it and re-query
        if not res:
            self._create_hydration_entry_for_today()
            res = self._notionClient.query_db(self._hydration_db, db_filter)

        self._set_hydration_level_of_page(res[0].get_id(), value)

    def _set_hydration_level_of_page(self, page_id: str, value: int):
        self._notionClient.set_page_property(page_id, 
            {"Amount (ml)": {"number": value}})

    def _create_hydration_entry_for_today(self):
        self._notionClient.create_page(self._hydration_db, 
            {"Date": {"date": {"start": date.today().isoformat()}},
             "Amount (ml)": {"number": 0}
            })
        
    






    