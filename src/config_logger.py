import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path("logs")


def setup_logger(log_dir=LOG_DIR):
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "parser.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s: - |%(levelname)s| %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(
                filename=log_file,
                maxBytes=1024 * 1024 * 5,
                backupCount=5,
                encoding="utf-8",
            ),
        ],
    )
