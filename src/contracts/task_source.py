from typing import Protocol, runtime_checkable
from collections.abc import Iterable

from src.contracts.task import Task


@runtime_checkable
class TaskSource(Protocol):
    name: str

    def get_tasks(self) -> Iterable[Task]: ...