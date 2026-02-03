import json
import logging
from pathlib import Path

from src.config_logger import setup_logger

setup_logger()
logger = logging.getLogger(__name__)


LOG_DIR = Path("data")


def save_to_json_file(contacts, filename, log_dir=LOG_DIR):
    log_dir.mkdir(exist_ok=True)
    file_path = log_dir / f"{filename}_contacts.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
        logger.info("JSON фаил был сохранён.")
