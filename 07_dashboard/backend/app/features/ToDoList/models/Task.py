from app.common.notion import NotionPage


class Task:

    @staticmethod
    def from_notion_page(page: NotionPage, initiative = None):
        task =  Task(
            name=page.get_str("Name")
            done=page.get_checkbox("Done")
            id=page.get_id()
        )
        if initiative:
            task.set_initiative(initiative)
    
    def __init__(self,
                 name: str,
                 done: bool,
                 id: str = None
                 ) -> None:
        self.Id = id
        self.Name = name
        self.Done = done
        self.Initiative = None

    def set_initiative(self, initiative):
        self.Initiative = initiative