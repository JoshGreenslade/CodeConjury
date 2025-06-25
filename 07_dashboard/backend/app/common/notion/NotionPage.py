from datetime import date

class NotionPage:

    def __init__(self, raw_page: dict):
        self._data = raw_page
        self._props = raw_page.get("properties", {})

    def get_id(self):
        return self._data["id"]
    
    def get_str(self, prop: str) -> str:
        prop_data = self._props.get(prop, {})
        for key in ("title", "rich_text"):
            blocks = prop_data.get(key, [])
            if isinstance(blocks, list) and len(blocks) > 0:
                return blocks[0].get("text", {}).get("content", "")
        return ""

    def get_date(self, prop: str):
        raw = self._props.get(prop, {}).get("date", {})
        if not raw:
            return
        start = raw.get("start")
        return date.fromisoformat(start) if start else None

    def get_number(self, prop: str):
        return self._props.get(prop, {}).get("number", None)
    
    def get_checkbox(self, prop: str):
        return self._props.get(prop, {}).get("checkbox", None)