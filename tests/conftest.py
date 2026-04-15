import pytest
from pathlib import Path
from typing import  Generator

# фикстура для модуля masks.py функция маскировки номера карт get_mask_card_number
@pytest.fixture
def card_data() -> list[tuple]:
    return [
        ("1234563212455632", "1234 56** **** 5632"),
        ("1234-5632-1245-5632", "1234 56** **** 5632"),
        ("1234-5632у1245у5632", "Не корректный ввод номера карты."),
        ("1234 5632 1245 5632", "1234 56** **** 5632"),
        ("123456321245563221321323", "Не корректный ввод номера карты."),
        ("", "Не корректный ввод номера карты."),
    ]


# фикстура для модуля masks.py функция маскировки счета get_mask_account
@pytest.fixture
def account_number() -> list[tuple]:
    return [
        ("1234563212455632", "**5632"),
        ("1234-5632-1245-5632", "**5632"),
        ("1234-5632у1245у5632", "Не корректный ввод номера счета."),
        ("1234 5632 1245 5632", "**5632"),
        ("", "Не корректный ввод номера счета."),
    ]


# фикстура для модуля widget.py маскировка номера или счета карт mask_account_card
@pytest.fixture
def card() -> list[tuple]:
    return [
        ("счет 12345678912345678912", "счет **8912"),
        ("VISA1254325698567854", "Некорректный формат данных, проверьте ввод."),
        ("12543 25698567854", "Некорректный формат данных, проверьте ввод."),
        ("VISA 1254325698567854", "VISA 1254 32** **** 7854"),
        ("123456321245563221321323", "Некорректный формат данных, проверьте ввод."),
        ("", "Некорректный формат данных, проверьте ввод."),
    ]


# фикстура для модуля widget.py преобразование даты get_date
@pytest.fixture
def g_date() -> list[tuple]:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("-2024-03-11T02:26:18.671407", "Ошибка ввода данных"),
        ("20-03-11T02:26:18.671407", "Ошибка ввода данных"),
        ("2024- -11T02:26:18.671407", "Ошибка ввода данных"),
        ("", "Ошибка ввода данных"),
    ]


# Фикстура для модуля processing.py для функции filter_by_state
@pytest.fixture
def date_list() -> list[dict]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


# Фикстура для модуля processing.py для функции sort_by_date
@pytest.fixture
def sample_data() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},  # Одинаковая дата
    ]


@pytest.fixture
def three_letters_str() -> str:
    return "asa"


@pytest.fixture
def empty_str() -> str:
    return ""


@pytest.fixture
def empty_list() -> list:
    return []


@pytest.fixture
def three_letters_list() -> list:
    return ["asa"]


@pytest.fixture
def transactions() -> list[dict]:
    """Фикстура с тестовыми транзакциями"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def log_filename() -> Generator:
    """Создает файл mylog.txt в корневой папке проекта"""
    temp_files_path = Path.cwd()
    filename = temp_files_path / "mylog.txt"

    # Создаем или очищаем файл
    with open(filename, "w") as f:
        f.write("")

    yield str(filename)  # Возвращаем строковый путь
