import pytest
from src.masks import get_mask_card_number


# Базовые тесты для функции
def test_get_mask_card_number():
    assert get_mask_card_number('1234563212455632') == '1234 56** **** 5632'
    assert get_mask_card_number('1234-5632-1245-5632') == '1234 56** **** 5632'
    assert get_mask_card_number('1234-5632у1245у5632') == 'Не корректный ввод номера карты.'
    assert get_mask_card_number('1234 5632 1245 5632') == '1234 56** **** 5632'
    assert get_mask_card_number('123456321245563221321323') == 'Не корректный ввод номера карты.'
    assert get_mask_card_number('') == 'Не корректный ввод номера карты.'


# Фикстура для создания тестовых данных
@pytest.fixture
def card_data():
    return [
        ('1234563212455632', '1234 56** **** 5632'),
        ('1234-5632-1245-5632', '1234 56** **** 5632'),
        ('1234-5632у1245у5632', 'Не корректный ввод номера карты.'),
        ('1234 5632 1245 5632', '1234 56** **** 5632'),
        ('123456321245563221321323', 'Не корректный ввод номера карты.'),
        ('', 'Не корректный ввод номера карты.')
    ]


#Проверка с фикстурой
def test_with_fixture(card_data):
    for card_number, expected in card_data:
        result = get_mask_card_number(card_number)
        assert result == expected


#Проверка  с параметризацией
@pytest.mark.parametrize("card_number, expected", [
    ('1234563212455632', '1234 56** **** 5632'),
    ('1234-5632-1245-5632', '1234 56** **** 5632'),
    ('1234-5632у1245у5632', 'Не корректный ввод номера карты.'),
    ('1234 5632 1245 5632', '1234 56** **** 5632'),
    ('123456321245563221321323', 'Не корректный ввод номера карты.'),
    ('', 'Не корректный ввод номера карты.')])

def test_with_parametrize(card_number, expected):
    result = get_mask_card_number(card_number)
    assert result == expected