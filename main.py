import argparse
import logging

from src.config_logger import setup_logger
from src.parser_contacts import parse_contacts
from src.service import save_to_json_file

setup_logger()
logger = logging.getLogger(__name__)


def main():
    logging.info('Парсер запущен')
    
    parser = argparse.ArgumentParser(description="Парсер контактов сайта")
    parser.add_argument(
        "start_url",
        type=str,
        help="URL сайта в форматe https://www.example.com",
    )
    args = parser.parse_args()
    logger.info(f'Аргументы командной строки: {args}')
    start_url = args.start_url
    contacts = parse_contacts(start_url)
    site_name = start_url.split(".")[1]
    save_to_json_file(contacts, site_name)
    print(contacts)
    logger.info(f"Парсинг контактов с сайта {start_url} завершён.")


if __name__ == "__main__":
    main()
