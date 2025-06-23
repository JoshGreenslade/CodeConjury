import os

class Config:
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    
    # Hydration
    NOTION_HYDRATION_DB_ID = os.getenv("NOTION_HYDRATION_DB_ID")

    # Habits
    NOTION_HABIT_CONFIG_DB_ID = os.getenv("NOTION_HABIT_CONFIG_DB_ID")
    NOTION_HABIT_TRACKER_DB_ID = os.getenv("NOTION_HABIT_TRACKER_DB_ID")