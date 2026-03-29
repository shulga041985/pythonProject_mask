import pytest
from src.masks import get_mask_card_number, get_mask_account


# Для тестирования функции маскировки номера карты
# Базовые тесты для функции
def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234563212455632") == "1234 56** **** 5632"
    assert get_mask_card_number("1234-5632-1245-5632") == "1234 56** **** 5632"
    assert get_mask_card_number("1234-5632у1245у5632") == "Не корректный ввод номера карты."
    assert get_mask_card_number("1234 5632 1245 5632") == "1234 56** **** 5632"
    assert get_mask_card_number("123456321245563221321323") == "Не корректный ввод номера карты."
    assert get_mask_card_number("") == "Не корректный ввод номера карты."


# Проверка с фикстурой
def test_fixture_card_number(card_data: list[tuple]) -> None:
    for card_number, expected in card_data:
        result = get_mask_card_number(card_number)
        assert result == expected


# Проверка  с параметризацией
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234563212455632", "1234 56** **** 5632"),
        ("1234-5632-1245-5632", "1234 56** **** 5632"),
        ("1234-5632у1245у5632", "Не корректный ввод номера карты."),
        ("1234 5632 1245 5632", "1234 56** **** 5632"),
        ("123456321245563221321323", "Не корректный ввод номера карты."),
        ("", "Не корректный ввод номера карты."),
    ],
)
def test_parametrize_card_number(card_number: str, expected: str) -> None:
    result = get_mask_card_number(card_number)
    assert result == expected


# Для тестирования функции маскировки номера счета
# Базовые тесты для функции
def test_get_mask_account() -> None:
    assert get_mask_account("1234563212455632") == "**5632"
    assert get_mask_account("1234-5632-1245-5632") == "**5632"
    assert get_mask_account("1234-5632у1245у5632") == "Не корректный ввод номера счета."
    assert get_mask_account("1234 5632 1245 5632") == "**5632"
    assert get_mask_account("") == "Не корректный ввод номера счета."



# Проверка с фикстурой
def test_fixture_account_number(account_number: list[tuple]) -> None:
    for acc_number, expected in account_number:
        result = get_mask_account(acc_number)
        assert result == expected


# Проверка  с параметризацией
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("1234563212455632", "**5632"),
        ("1234-5632-1245-5632", "**5632"),
        ("1234-5632у1245у5632", "Не корректный ввод номера счета."),
        ("1234 5632 1245 5632", "**5632"),
        ("", "Не корректный ввод номера счета."),
    ],
)
def test_parametrize_account_number(account_number: str, expected: str) -> None:
    result = get_mask_account(account_number)
    assert result == expected
