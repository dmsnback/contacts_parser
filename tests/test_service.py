import json

import pytest

from src.service import save_to_json_file


@pytest.fixture
def contacts_for_test():
    test_contacts = {
        "url": "https://www.example.com",
        "phones": ["8-900-777-66-55"],
        "emails": ["example_1@mail.com", "example_2@mail.ru"],
    }
    return test_contacts


def test_save_to_json_file(contacts_for_test, tmp_path):
    """Тестируется сохранение файла и его правильное наполнение"""
    filename = "test_contacts"
    save_to_json_file(contacts_for_test, filename, log_dir=tmp_path)
    file_path = tmp_path / "test_contacts_contacts.json"
    assert file_path.exists(), "Файл не был создан."
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    assert (
        data == contacts_for_test
    ), "Данные в JSON файле не соответствуют ожидаемым."
