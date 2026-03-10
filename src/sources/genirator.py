import uuid

from collections.abc import Iterable
from dataclasses import dataclass

from src.contracts.task import Task


@dataclass(frozen=True)
class GenSource:
    count_gen_tasks: int
    name: str = "gen"

    def get_tasks(self) -> Iterable[Task]:
        """
        Создает задачи и отправляет их
        :param argumentes: None
        :return: Iterable[Task]
        """
        for i in range(1, self.count_gen_tasks + 1):

            task_id = str(uuid.uuid4()) # создает id
            task_text = f"Сгенерирована задача номер {i}"

            yield Task(
                id=task_id, text=task_text
            )
