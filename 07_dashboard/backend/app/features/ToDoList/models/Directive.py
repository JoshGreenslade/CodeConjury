
from typing import List
from app.common.notion import NotionPage

class Directive:
    
    @staticmethod
    def from_notion_page(page: NotionPage):
        directive = Directive(
            name=page.get_str("Name"),
            done=page.get_checkbox("Done"),
            isActive=page.get_checkbox("IsActive"),
            description=page.get_str("Description"),
            id=page.get_id()
        )
        return directive

    def __init__(self,
                 name: str,
                 done: bool,
                 isActive: bool,
                 description: str,
                 id: str = None
                 ) -> None:
        self.Id = id
        self.Name = name
        self.Done = done
        self.IsActive = isActive
        self.Description = description
        self.Initatives = []

    def set_initiatives(self, initiatives):
        self.Initiatives = initiatives
