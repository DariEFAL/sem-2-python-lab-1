from collections.abc import Sequence, Iterable

from src.contracts.task_source import TaskSource
from src.contracts.task import Task

class InboxApp:
    """Есть список рессурсов откуда поступают задачи и он их отправляет из разных источников"""
    def __init__(self, sources: Sequence[TaskSource] = None):
        self._sources = sources or []

    def iter_task(self) -> Iterable[Task]:
        for source in self._sources:
            if not isinstance(source, TaskSource):
                raise TypeError(f"Источник должен быть типа TaskSource")
            
            for task in source.get_tasks():
                yield task