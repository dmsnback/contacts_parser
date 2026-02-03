import json
import logging
from pathlib import Path

from src.config_logger import setup_logger


setup_logger()
logger = logging.getLogger(__name__)


LOG_DIR = Path("data")
LOG_DIR.mkdir(exist_ok=True)


def save_to_json_file(contacts, filename):
    with open(
        f"{LOG_DIR}/{filename}_contacts.json", "w", encoding="utf-8"
    ) as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)
        logger.info(f'JSON фаил был сохранён.')
