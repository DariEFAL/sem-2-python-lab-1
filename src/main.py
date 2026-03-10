import sys

from src.cli import cli
from src.logging import logging_result


def main():
    """
    Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    try:
        cli()
    except SystemExit as error:
        if error.code != 0:
            error_text = ' '.join(sys.argv[1:])
            logging_result(False, id=None, error_text=f"Неправильный ввод команды: {error_text}")
            print(f"Неправильный ввод команды: {error_text}", file=sys.stderr)
            sys.exit(1)

        raise


if __name__ == "__main__":
    main()