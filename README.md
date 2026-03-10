# Лабораторная работа 1, семестр 2, python.

```
 git clone https://github.com/DariEFAL/sem-2-python-lab-1.git
 cd sem-2-python-lab-1
 uv venv
 source .venv/bin/activate
 (Для windows: .venv\Scripts\Activate.ps1)

 Установка зависимостей:
 uv pip install -e .

 Вызов тестов: 
 pytest tests -v

 Вызов программы: python -m main 
```

# Источники задач:
* jsonl: python -m main --jsonl *путь к файлу*
* stdin: python -m main --stdin
* genirator: python -m main --gen *кол-во задач, которые надо сгенерировать*

# Принятые решения:
* cli реализован через typer
* Задачи из всех источников получают новое id, даже если есть старое. Реализовано спомощью uuid.uuid4() 
* 