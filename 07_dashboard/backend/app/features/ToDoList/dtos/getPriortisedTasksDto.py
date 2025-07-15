from dataclasses import dataclass
from typing import List

@dataclass
class getPrioritisedTasksDto:
    results: List

@dataclass
class Task:
    effort: int
    reason: str
    task_id: str
    title: str
    