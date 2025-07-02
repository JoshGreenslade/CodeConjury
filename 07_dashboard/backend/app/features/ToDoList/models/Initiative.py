
from app.common.notion import NotionPage


class Initiative:
    
    @staticmethod
    def from_notion_page(page: NotionPage, directive=None, tasks=None):
        initiative =  Initiative(
            name=page.get_str("Name"),
            done=page.get_checkbox("Done"),
            isActive=page.get_checkbox("IsActive"),
            description=page.get_str("Description")
        )
        if directive:
            initiative.set_directive(directive)
        if tasks:
            initiative.set_tasks(tasks)
        return initiative

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
        self.Tasks = []
        self.Directive = None

    def set_tasks(self, tasks):
        self.Tasks = tasks

    def set_directive(self, directive):
        self.Directive = directive
