import sys
from dataclasses import dataclass
from typing import TextIO
from collections.abc import Iterable

from src.contracts.task import Task


def check_stdin(task: list[str], line_number: int):
    try:
        return task[0], task[1] 
    except ValueError:
        raise ValueError(f"строка: {line_number}: задача состоит только из двух аргументов: id и text")


@dataclass(frozen=True)
class StdinSource:
    stream: TextIO = sys.stdin
    name: str = "stdin"

    def get_tasks(self) -> Iterable[Task]:
        for line_number, line in enumerate(self.stream):
            line = line.strip().split(":")

            if not line:
                continue

            task_id, task_text = check_stdin(line, line_number)
            
            yield Task(
                id=task_id, text=task_text
            )