import pytest
from src.widget import mask_account_card, get_date


# Для тестирования функции маскировки номера карты
# Базовые тесты для функции
def test_mask_account_card() -> None:
    assert mask_account_card("счет 12345678912345678912") == "счет **8912"
    assert mask_account_card("VISA1254325698567854") == "Некорректный формат данных, проверьте ввод."
    assert mask_account_card("12543 25698567854") == "Некорректный формат данных, проверьте ввод."
    assert mask_account_card("VISA 1254325698567854") == "VISA 1254 32** **** 7854"
    assert mask_account_card("123456321245563221321323") == "Некорректный формат данных, проверьте ввод."
    assert mask_account_card("") == "Некорректный формат данных, проверьте ввод."


# Проверка с фикстурой
def test_fixture_account_card(card: list[tuple]) -> None:
    for card_details, expected in card:
        result = mask_account_card(card_details)
        assert result == expected


# Проверка  с параметризацией
@pytest.mark.parametrize(
    "card_details, expected",
    [
        ("счет 12345678912345678912", "счет **8912"),
        ("VISA1254325698567854", "Некорректный формат данных, проверьте ввод."),
        ("12543 25698567854", "Некорректный формат данных, проверьте ввод."),
        ("VISA 1254325698567854", "VISA 1254 32** **** 7854"),
        ("123456321245563221321323", "Некорректный формат данных, проверьте ввод."),
        ("", "Некорректный формат данных, проверьте ввод."),
    ],
)
def test_parametrize_account_card(card_details: str, expected: str) -> None:
    result = mask_account_card(card_details)
    assert result == expected


# Для тестирования функции маскировки номера счета
# Базовые тесты для функции
def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("-2024-03-11T02:26:18.671407") == "Ошибка ввода данных"
    assert get_date("20-03-11T02:26:18.671407") == "Ошибка ввода данных"
    assert get_date("2024- -11T02:26:18.671407") == "Ошибка ввода данных"
    assert get_date("") == "Ошибка ввода данных"


# Проверка с фикстурой
def test_get(g_date: list[tuple]) -> None:
    for date, expected in g_date:
        result = get_date(date)
        assert result == expected


# Проверка  с параметризацией
@pytest.mark.parametrize(
    "input_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("-2024-03-11T02:26:18.671407", "Ошибка ввода данных"),
        ("20-03-11T02:26:18.671407", "Ошибка ввода данных"),
        ("2024- -11T02:26:18.671407", "Ошибка ввода данных"),
        ("", "Ошибка ввода данных"),
    ],
)
def test_parametrize_get_date(input_date: str, expected: str) -> None:
    result = get_date(input_date)
    assert result == expected
