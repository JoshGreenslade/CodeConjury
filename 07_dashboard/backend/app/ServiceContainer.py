from app.common.notion.notion_client import NotionClient

class ServiceContainer:
    def __init__(self, config):
        self.notion_client = NotionClient(api_key=config["NOTION_API_KEY"])
