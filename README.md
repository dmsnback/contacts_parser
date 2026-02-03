<a name="Начало"></a>

## Contacts Parser

[![Contacts Parser Lint and Tests](https://img.shields.io/github/actions/workflow/status/dmsnback/contacts_parser/main.yml?branch=main&style=flat-square&label=Contacts%20Parser%20Lint%20and%20Tests)](https://github.com/dmsnback/contacts_parser/actions/workflows/main.yml)
![Python](https://img.shields.io/badge/python-3.11-blue)
![Tests](https://img.shields.io/badge/tests-pytest-brightgreen)
![Black](https://img.shields.io/badge/code%20style-black-000000)

- [Описание](#Описание)
- [Технологии](#Технологии)
- [Тестирование](#Тестирование)
- [Запуск проекта на локальной машине](#Запуск)
- [Автор](#Автор)

<a name="Описание"></a>

### Описание

Мини-проект на Python для парсинга контактов сайта.

Возможности:

```md
- Загружает страницы сайта
- Переходит по внутренним ссылкам
- Ищет email и номера телефонов
- Сохраняет результат в JSON
- Логирует процесс работы
- Покрыт тестами (pytest)
```

Парсер написан с использованием **Beautiful Soup 4** и **Requests**.

В проекте настроен **CI pipeline** с использованием **GitHub Actions**:

```md
- Автоматическая проверка кода (black, isort, flake8)
- Запуск unit-тестов (`pytest`)
```

> [Вернуться в начало](#Начало)

<a name="Технологии"></a>

### Технологии

[![Python](https://img.shields.io/badge/Python-1000?style=for-the-badge&logo=python&logoColor=ffffff&labelColor=000000&color=000000)](https://www.python.org)
[![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-1000?style=for-the-badge&logo=&logoColor=ffffff&labelColor=000000&color=000000)](https://beautiful-soup.readthedocs.io/en/latest/)
[![Requests](https://img.shields.io/badge/Requests-1000?style=for-the-badge&logo=Requests&logoColor=ffffff&labelColor=000000&color=000000)](https://requests.readthedocs.io/en/latest/index.html)
[![Pytest](https://img.shields.io/badge/Pytest-1000?style=for-the-badge&logo=pytest&logoColor=ffffff&labelColor=000000&color=000000)](https://docs.pytest.org/en/stable/index.htmlc)
[![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=ffffff&labelColor=000000&color=000000)](https://github.com/features/actions)

> [Вернуться в начало](#Начало)

<a name="Тестирование"></a>

### Тестирование

В проекте реализованы **unit-тесты** с использованием `pytest`.

Запуск тестов локально:

```python
pytest -v
```

> [Вернуться в начало](#Начало)

<a name="Запуск"></a>

### Запуск проекта на локальной машине

- Склонируйте репозиторий

```python
git clone git@github.com:dmsnback/contacts_parser.git
```

- Установите и активируйте виртуальное окружение

```python
python3 -m venv venv
```

Для `Windows`

```python
source venv/Scripts/activate
```

Для `Mac/Linux`

```python
source venv/bin/activate
```

- Установите зависимости из файла
`requirements.txt`

```python
python3 -m pip install --upgrade pip
```

```python
pip install -r requirements.txt
```

- Запускаем проект, при запуске передаем аргумент в виде https://www.example.com

```python
python3 main.py https://www.lenta.ru         
```

- После запуска появиттся папка data с json файлом и в терминале появится результат парсинга в виде:

```md
{
  "url": "https://www.lenta.ru",
  "phones": ["8-900-777-66-55"],
  "emails": ["example@mail.ru"]
}
```

> [Вернуться в начало](#Начало)

<a name="Автор"></a>
