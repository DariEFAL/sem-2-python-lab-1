import json
import uuid

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
        logging_result(False, id=None, error_text=f"Неправильный ввод jsonl в {path} в строке {line_number}")
        print(f"Неправильный ввод jsonl в {path} в строке {line_number}")
        return {"error": f"Неправильный ввод jsonl в {path} в строке {line_number}"}


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
                if "error" in task:
                    continue

                task_id = str(uuid.uuid4()) # создает новое id
                task_text = task.get("text", "")

                yield Task(
                    id=task_id, text=task_text
                )

