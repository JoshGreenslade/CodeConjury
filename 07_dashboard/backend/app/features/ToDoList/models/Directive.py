
from app.common.notion import NotionPage


class Directive:
    
    @staticmethod
    def from_notion_page(page: NotionPage, initiatves=None):
        directive = Directive(
            name=page.get_str("Name"),
            done=page.get_checkbox("Done"),
            isActive=page.get_checkbox("IsActive"),
            description=page.get_str("Description")
        )
        if initiatves:
            directive.set_initiatives(initiatves)
        return directive

    def __init__(self,
                 name: str,
                 done: bool,
                 isActive: bool,
                 description: str,
                 ) -> None:
        self.Name = name
        self.Done = done
        self.IsActive = isActive
        self.Description = description
        self.Initatives = []

    def set_initiatives(self, initiatives):
        self.Initiatives = initiatives
