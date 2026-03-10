import json
from collections.abc import Iterable
from pathlib import Path
from dataclasses import dataclass

from src.contracts.task import Task
from src.logging import logging_result


def parse_json_file(line: str, path: Path, line_number: int) -> dict[str, str]:
    """Делает из строки словарь"""
    try:
        return json.loads(line)
    except json.JSONDecodeError as error:
        logging_result(False, id=None, error_text=f"Плохой ввод json в {path} в строке {line_number}")
        raise ValueError(f"Плохой ввод json в {path} в строке {line_number}: {error}") from error


@dataclass(frozen=True)
class JsonSource:
    path: Path
    name: str = "file-jsonl"

    def get_tasks(self) -> Iterable[Task]:
        """
        Возвращает задачи полученные из jsonl
        :param argumentes: None
        :return: Iterable[Task]
        """
        with self.path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                task = parse_json_file(line, self.path, line_number)
                task_id = task.get("id", f"{self.path.name}:{line_number}")
                task_text = task.get("text", "")

                yield Task(
                    id=task_id, text=task_text
                )

