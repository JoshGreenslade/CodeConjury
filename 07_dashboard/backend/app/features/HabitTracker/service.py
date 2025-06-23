from flask import Flask
from app.ServiceContainer import ServiceContainer
from datetime import date, datetime, time
from croniter import croniter

class HabitService:
    def __init__(self, app: Flask, services: ServiceContainer):
        self._notionClient = services.notion_client
        self._habit_config_db = app.config["NOTION_HABIT_CONFIG_DB_ID"]
        self._habit_tracker_db = app.config["NOTION_HABIT_TRACKER_DB_ID"]

    def get_todays_habits(self):
        self._create_overdue_habits()
        db_filter = {
            "property": "Created Date",
            "date": {"equals": date.today().isoformat()}
            }
        habits = self._notionClient.query_db(self._habit_tracker_db, db_filter)
        return habits

    def _get_habit_config(self):
        return self._notionClient.query_db(self._habit_config_db)

    def _add_habit_page(self, habit):
        habit_properties = {
            "Habit": {"title": [{"text": {"content": habit.get_str("Habit")}}]},
            "Checkbox": {"checkbox": False},
            "Created Date": {"date": {"start": date.today().isoformat()}}
        }
        self._notionClient.create_page(self._habit_tracker_db, habit_properties)

    def _create_overdue_habits(self):
        habits_to_create = self._get_habits_due_for_creation()
        for habit in habits_to_create:
            self._add_habit_page(habit)
            self._notionClient.set_page_property(habit.get_id(),{
                "Last Added": {"date": {"start": date.today().isoformat()}}
            })
    
    def _get_habits_due_for_creation(self):
        habits = self._get_habit_config()
        habits_due_for_creation = []
        for habit in habits:
            cron = habit.get_str("Cron")
            last_added = datetime.combine(habit.get_date("Last Added") or date.min, time.min)
            next_due = croniter(cron, last_added).get_next(datetime)
            print(next_due.date())
            if next_due.date() <= date.today():
                habits_due_for_creation.append(habit)
        return habits_due_for_creation









    