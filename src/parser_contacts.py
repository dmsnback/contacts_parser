import logging
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from src.config_logger import setup_logger
from src.found_contacts import found_emails, found_phones

setup_logger()
logger = logging.getLogger(__name__)


def parse_contacts(start_url, max_pages=50):
    visited_page = set()
    to_visit = [start_url]
    emails = set()
    phones = set()
    domain = urlparse(start_url).netloc

    while to_visit and len(visited_page) < max_pages:
        url = to_visit.pop()
        if url in visited_page:
            continue
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Ошибка при загрузке страницы: {e}")
            continue

        visited_page.add(url)
        try:
            soup = BeautifulSoup(response.text, "lxml")
            text_html = soup.get_text()
        except Exception as e:
            logger.error(f"Ошибка при парсинге страницы {url}: {e}")

        all_emails = found_emails(text_html)
        all_phones = found_phones(text_html)

        emails.update(all_emails)
        phones.update(all_phones)

        all_links = soup.find_all("a", href=True)
        for link in all_links:
            href = link["href"]
            full_link = urljoin(url, href)
            if (
                urlparse(full_link).netloc == domain
                and full_link not in visited_page
            ):
                to_visit.append(full_link)

    contacts = {
        "url": start_url,
        "emails": list(emails),
        "phones": list(phones),
    }

    return contacts
