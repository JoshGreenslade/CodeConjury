import os

class Config:
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    
    # Hydration
    NOTION_HYDRATION_DB_ID = os.getenv("NOTION_HYDRATION_DB_ID")

    # Habbits
    NOTION_HABBIT_DB_ID = os.getenv("NOTION_HABBIT_DB_ID")