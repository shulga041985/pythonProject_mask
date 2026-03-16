from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

"""Для маскировки карты и счета"""

card_details = "счет 1254325698567854"  # номера карты или счета
masked_card = mask_account_card(card_details)

print(masked_card)

"""Для преобразования формата даты"""

input_date = "2024-03-11T02:26:18.671407"  # входной формат даты
correct_date = get_date(input_date)

print(correct_date)

"""Для работы со списком словарей банковских операций"""
date_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


key_test = filter_by_state(date_list, state="EXECUTED")  # проверка на вывод по ключу state
print(key_test)


sort_test = sort_by_date(date_list, True)  # сортировка ко ключу date
print(sort_test)
