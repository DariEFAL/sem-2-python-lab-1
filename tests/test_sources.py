from pathlib import Path
from io import StringIO

from src.contracts.task_source import TaskSource
from src.contracts.task import Task
from src.sources.genirator import GenSource
from src.sources.json import JsonSource
from src.sources.stdin import StdinSource
from src.inbox.core import InboxApp


def test_source():
    """Проверка, что источники следует протоколу TaskSource"""
    assert isinstance(GenSource, TaskSource) == True
    assert isinstance(JsonSource, TaskSource) == True
    assert isinstance(StdinSource, TaskSource) == True


def test_get_tasks():
    """Проверка, что get_tasks и InboxApp возвращает задачи в нужном формате"""
    source1 = GenSource(3)
    for task in source1.get_tasks():
        assert isinstance(task, Task) == True

    source2 = JsonSource(Path("./source/tasks.jsonl"))
    for task in source2.get_tasks():
        assert isinstance(task, Task) == True

    fake_stream = StringIO("23:task23\n34:task34")
    source3 = StdinSource(stream=fake_stream)
    for task in source3.get_tasks():
        assert isinstance(task, Task) == True

    sources = InboxApp([source1, source2, source3])
    for task in sources.iter_task():
        assert isinstance(task, Task) == True

    

    