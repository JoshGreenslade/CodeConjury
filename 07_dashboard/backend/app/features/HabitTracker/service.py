from typing import List
from flask import Flask
from app.ServiceContainer import ServiceContainer
from datetime import date, datetime, time
from croniter import croniter

from app.common.notion import NotionPage
from .dtos.getHabitDto import getHabitDto

NOTION_HABIT_CONFIG_DB_ID = "NOTION_HABIT_CONFIG_DB_ID"
NOTION_HABIT_TRACKER_DB_ID = "NOTION_HABIT_TRACKER_DB_ID"
HABIT_NAME_KEY = "Habit"
HABIT_CHECKED_KEY = "Completed"
HABIT_CREATED_KEY = "Created Date"
HABIT_CRON_KEY = "Cron"
HABIT_LAST_ADDED_KEY = "Last Added"

class HabitService:
    def __init__(self, app: Flask, services: ServiceContainer):
        self._notionClient = services.notion_client
        self._habit_config_db = app.config[NOTION_HABIT_CONFIG_DB_ID]
        self._habit_tracker_db = app.config[NOTION_HABIT_TRACKER_DB_ID]

    def get_todays_habits(self) -> list[getHabitDto]:
        self._create_overdue_habits()
        config = self._get_habit_config()
        habits = self._get_habits_created_today()
        habits_dto = [getHabitDto(
            Habit=habit.get_str(HABIT_NAME_KEY),
            Checked=habit.get_checkbox(HABIT_CHECKED_KEY),
            Url=None
        ) for habit in habits]
        for habit in habits_dto:
            matching_config = [i for i in config if i.get_str(HABIT_NAME_KEY) == habit.Habit]
            habit.Url = matching_config[0].get_url()
        return habits_dto
    
    def set_habit_completion(self, habit_name: str, completed: bool):
        habits = self._get_habits_created_today()
        habit = next(i for i in habits if i.get_str(HABIT_NAME_KEY) == habit_name)
        self._notionClient.set_page_property(habit.get_id(), {
            HABIT_CHECKED_KEY: {"checkbox": completed}
        })

    # ===== Private ===== 

    def _get_habit_config(self):
        return self._notionClient.query_db(self._habit_config_db)

    def _add_habit_page(self, habit):
        habit_properties = {
            HABIT_NAME_KEY: {"title": [{"text": {"content": habit.get_str(HABIT_NAME_KEY)}}]},
            HABIT_CHECKED_KEY: {"checkbox": False},
            HABIT_CREATED_KEY: {"date": {"start": date.today().isoformat()}}
        }
        self._notionClient.create_page(self._habit_tracker_db, habit_properties)

    def _create_overdue_habits(self):
        habits_to_create = self._get_habits_due_for_creation()
        for habit in habits_to_create:
            self._add_habit_page(habit)
            self._notionClient.set_page_property(habit.get_id(),{
                HABIT_LAST_ADDED_KEY : {"date": {"start": date.today().isoformat()}}
            })
    
    def _get_habits_created_today(self) -> List[NotionPage.NotionPage] | None:
        db_filter = {
            "property": HABIT_CREATED_KEY,
            "date": {"equals": date.today().isoformat()}
            }
        habits = self._notionClient.query_db(self._habit_tracker_db, db_filter)
        return habits
    
    def _get_habits_due_for_creation(self):
        habits = self._get_habit_config()
        habits_due_for_creation = []
        for habit in habits:
            cron = habit.get_str(HABIT_CRON_KEY)
            last_added = datetime.combine(habit.get_date(HABIT_LAST_ADDED_KEY) or date.min, time.min)
            next_due = croniter(cron, last_added).get_next(datetime)
            if next_due.date() <= date.today():
                habits_due_for_creation.append(habit)
        return habits_due_for_creation