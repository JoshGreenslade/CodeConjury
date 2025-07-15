from dataclasses import dataclass
from typing import Optional

@dataclass
class getHabitDto:
    Habit: str
    Checked: bool
    Url: Optional[str]
