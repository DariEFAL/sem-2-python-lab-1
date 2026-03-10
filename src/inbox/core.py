import uuid

from collections.abc import Sequence, Iterable

from src.contracts.task_source import TaskSource
from src.contracts.task import Task
from src.logging import logging_result


class InboxApp:
    def __init__(self, sources: Sequence[TaskSource] = None):
        self.sources = sources or []

    def iter_task(self) -> Iterable[Task]:
        """
        Возвращает задачи из разных источников
        :param argumentes: None
        :return: Iterable[Task]
        """
        for source in self.sources:
            if not isinstance(source, TaskSource):
                logging_result(False, id=None, error_text="Источник должен быть типа TaskSource")
                raise TypeError("Источник должен быть типа TaskSource")
            
            for task in source.get_tasks():
                logging_result(True, id=task.id)
                yield task