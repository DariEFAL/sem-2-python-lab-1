import sys
from dataclasses import dataclass
from typing import TextIO
from collections.abc import Iterable

from src.contracts.task import Task
from src.logging import logging_result


def check_stdin(task: list[str], line_number: int) -> dict[str, str]:
    """Проверяет данные, которые ввел пользователь"""
    try:
        return {"id": task[0], "text": task[1]}
    except ValueError:
        logging_result(False, id=None, error_text=f"Неправильный ввод stdin в строке {line_number}: задача может состоять только из двух аргументов: id и text")
        print(f"Неправильный ввод stdin в строке {line_number}: задача может состоять только из двух аргументов: id и text")
        return {"error": f"Неправильный ввод stdin в строке {line_number}: задача может состоять только из двух аргументов: id и text"}


@dataclass(frozen=True)
class StdinSource:
    stream: TextIO = sys.stdin
    name: str = "stdin"

    def get_tasks(self) -> Iterable[Task]:
        """
        Возвращает задачи полученные из stdin
        :param argumentes: None
        :return: Iterable[Task]
        """
        for line_number, line in enumerate(self.stream):
            line = line.strip().split(":")

            if not line:
                continue

            task = check_stdin(line, line_number)
            if "error" in task:
                    continue
                
            task_id = task.get("id", "")
            task_text = task.get("text", "")
            
            yield Task(
                id=task_id, text=task_text
            )