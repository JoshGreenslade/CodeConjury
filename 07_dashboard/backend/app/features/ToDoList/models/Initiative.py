
from typing import List
from app.common.notion import NotionPage


class Initiative:
    
    @staticmethod
    def from_notion_page(page: NotionPage):
        initiative =  Initiative(
            id = page.get_id(),
            name=page.get_str("Name"),
            done=page.get_checkbox("Done"),
            isActive=page.get_checkbox("IsActive"),
            description=page.get_str("Description"),
            directiveId=page.get_relation("Directive")[0]["id"]
        )
        return initiative

    def __init__(self,
                 name: str,
                 done: bool,
                 isActive: bool,
                 description: str,
                 directiveId: str,
                 id: str = None
                 ) -> None:
        self.Id = id
        self.Name = name
        self.Done = done
        self.IsActive = isActive
        self.Description = description
        self.Tasks = []
        self.DirectiveId = directiveId
        self.Directive = None

    def set_tasks(self, tasks):
        self.Tasks = tasks

    def set_directive(self, directive):
        self.Directive = directive
