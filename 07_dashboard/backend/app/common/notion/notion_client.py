from notion_client import Client
from .NotionPage import NotionPage

class NotionClient: 
    def __init__(self, api_key):
        self._notion = Client(auth=api_key)

    def query_db(self, db: str, db_filter: dict = None):

        if db_filter:        
            print("with filter")
            print(db_filter)    
            res = self._notion.databases.query(
                database_id=db,
                filter = db_filter
            )
        else:
            res = self._notion.databases.query(database_id=db)
        if not res:
            return None
        result = [NotionPage(i) for i in res.get("results", [])]
        return result
    
    def set_page_property(self, page_id: str, properties: dict):
        self._notion.pages.update(page_id=page_id, properties=properties)

    def create_page(self, db_id: str, properties: dict):
        self._notion.pages.create(parent={"database_id": db_id}, 
                                  properties=properties)