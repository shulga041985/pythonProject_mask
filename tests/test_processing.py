import pytest

# from typing import List, Dict,Any
from src.processing import filter_by_state, sort_by_date


# тесты для  фильтрации по статусу
@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("NON_EXISTENT", []),
    ],
)
# параметризированый тест по статусу включая пустой список
def test_filter_by_state(date_list: list[dict], state: str, expected: list[dict]) -> None:
    result = filter_by_state(date_list, state)
    assert result == expected


def test_filter_by_nonexistent_state(date_list: list[dict]) -> None:
    """Тестирование фильтрации по статусу, отсутствующему в списке"""
    # Пытаемся отфильтровать по несуществующему статусу
    filtered = filter_by_state(date_list, "PENDING")

    # Ожидаем пустой список
    assert filtered == []
    assert isinstance(filtered, list)


# Тест сортировки по дате по дате
@pytest.mark.parametrize(
    "date, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),  # Убывающий порядок
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),  # Возрастающий порядок
    ],
)
def test_sort_by_date_order(sample_data: list[dict], date: bool, expected: list[dict]) -> None:
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""
    sorted_operations = sort_by_date(sample_data, date)
    assert sorted_operations == expected


def test_list() -> None:
    """Тест с пустым списком"""
    result = sort_by_date([])
    assert result == []


def test_consistent_output_type(sample_data: list[dict]) -> None:
    """Тест, что функция всегда возвращает список словарей"""
    result = sort_by_date(sample_data)
    assert isinstance(result, list)
    for item in result:
        assert isinstance(item, dict)
        assert "date" in item
