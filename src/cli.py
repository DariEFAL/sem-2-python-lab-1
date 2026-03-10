from pathlib import Path
from typing import Any

import typer

from src.inbox.core import InboxApp
from src.sources.json import JsonSource
from src.sources.genirator import GenSource
from src.sources.stdin import StdinSource

cli = typer.Typer()

@cli.command("read")
def read(
    jsonl: list[Path] = typer.Option(
        help="Read task from file jsonl",
        default_factory=list,
        exists=True,
        dir_okay=False,
        readable=True,
    ),
    gen: list[int] = typer.Option(
        help="Read task from gen",
        default_factory=list,
        min=1
    ),
    stdin: bool = typer.Option(False, "--stdin", help="Read task from stdin"),):

    sources: list[Any] = []

    if stdin:
        sources.append(StdinSource())

    for path in jsonl:
        sources.append(JsonSource(path))

    for count in gen:
        sources.append(GenSource(count))
    
    inbox = InboxApp(sources)
    task_count = 0
    for task in inbox.iter_task():
        task_count += 1
        typer.echo(f"{task.id}: {task.text}")
    
    typer.echo(f"Всего задач: {task_count}")

