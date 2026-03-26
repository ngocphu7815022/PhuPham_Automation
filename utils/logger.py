import logging
import os

def get_project_root():
    current = os.path.abspath(__file__)
    while current != "/":
        if os.path.exists(os.path.join(current, "pytest.ini")):
            return current
        current = os.path.dirname(current)
    raise RuntimeError("pytest.ini not found. Project root not detected.")

PROJECT_ROOT = get_project_root()
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # Console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)

        # File
        os.makedirs(LOG_DIR, exist_ok=True)
        log_file = os.path.join(LOG_DIR, "test.log")

        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        logger.propagate = False

    return logger
