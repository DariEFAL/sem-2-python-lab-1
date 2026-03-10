import logging


logging.basicConfig(level=logging.INFO,
                    filename="tasks.log",
                    format="[%(asctime)s] %(levelname)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    encoding="utf-8")

logger = logging.getLogger("tasks")


def logging_result(result: bool, id: str = None, error_text: str = None):
    if result:
        logger.info(f"Задача {id} успешно обработана")
    else:
        logger.error(f"{error_text}")