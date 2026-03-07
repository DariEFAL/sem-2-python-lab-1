from pathlib import Path

import typer

from src.inbox.core import InboxApp
from src.sources.json import JsonSource

cli = typer.Typer(no_args_is_help=True) # параметр, чтобы если пользователь запустил без арг, то показалась справка

@cli.command("read")
def read(
    jsonl: list[Path] = typer.Option(
        help="Read task from file jsonl",
        default_factory=list,
        exists=True,
        dir_okay=False,
        readable=True,
    ),):

    sources = []
    for path in jsonl:
        sources.append(JsonSource(path))
    
    inbox = InboxApp(sources)
    for task in inbox.iter_task():
        typer.echo(f"{task.id}: {task.text}")
