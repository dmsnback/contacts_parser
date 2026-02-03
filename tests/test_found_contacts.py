import pytest

from src.found_contacts import found_emails, found_phones


@pytest.fixture
def text_with_contacts():
    test_text = "Можете писать нам на почту: test_1@mail.com, test_2@mail.ru, либо по телефону: 8(900)777-66-55"
    return test_text


@pytest.fixture
def text_without_contacts():
    test_text = "Зддесь нет email и номеера телефона"
    return test_text


def test_found_email(text_with_contacts):
    result = found_emails(text_with_contacts)
    assert "test_1@mail.com" in result, "Не найдена почта test_1@mail.com"
    assert "test_2@mail.ru" in result, "Не найдена почта test_2@mail.ru"
    assert (
        len(result) == 2
    ), f"Количество найденных email - {len(result)} не соответствует ожидаемому - 2."


def test_found_phone(text_with_contacts):
    result = found_phones(text_with_contacts)
    assert (
        "8(900)777-66-55" in result
    ), "Не найдена номер телефона 8(900)777-66-55"
    assert (
        len(result) == 1
    ), f"Количество найденных телефонных номеров - {len(result)} не соответствует ожидаемому - 1."


def test_found_email_empty(text_without_contacts):
    result = found_emails(text_without_contacts)
    assert (
        len(result) == 0
    ), "Функция должна возвращать пустой список, если нет почты."


def test_found_phone_empty(text_without_contacts):
    result = found_phones(text_without_contacts)
    assert (
        len(result) == 0
    ), "Функция должна возвращать пустой список, если нет номера телефона."
