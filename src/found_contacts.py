import re

REGEX_EMAIL = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
REGEX_PHONE = r"(?:\+7|8)\s*\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}"


def found_emails(text):
    """Ищет email тексте"""
    emails = re.findall(REGEX_EMAIL, text)
    return emails


def found_phones(text):
    """Ищет номера телефонов тексте"""
    phones = re.findall(REGEX_PHONE, text)
    return phones
