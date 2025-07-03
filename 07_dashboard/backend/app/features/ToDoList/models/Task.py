from app.common.notion import NotionPage


class Task:

    @staticmethod
    def from_notion_page(page: NotionPage):
        task =  Task(
            id=page.get_id(),
            name=page.get_str("Name"),
            done=page.get_checkbox("Done"),
            initiativeId=page.get_relation("Initiative")[0]["id"]
        )
        return task
    
    def __init__(self,
                 name: str,
                 done: bool,
                 initiativeId: str,
                 id: str = None
                 ) -> None:
        self.Id = id
        self.Name = name
        self.Done = done
        self.InitiativeId = initiativeId
        self.Initiative = None

    def set_initiative(self, initiative):
        self.Initiative = initiative