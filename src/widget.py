from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_details: str) -> str:
    """Принимает  номер счёта или карты, маскировка в зависимости от данных"""
    part_name = card_details.split()  # разбиваем по пробелу
    if part_name[-1].isdigit():  # забираем -1 индекс и проверяем что только цифры
        number = int(part_name[-1])  # оборачиваем в целые числа
    else:
        return "Номер не состоит из цифр, введите корректный номер"
    initials = " ".join(part_name[:-1])  # делаем срез до - 1 индекса
    if initials.upper() == "СЧЕТ":  # проверка на вхождение
        masks_number = get_mask_account(number)
    else:
        masks_number = get_mask_card_number(number)
    return f"{initials} {masks_number}"


def get_date(input_date: str) -> str:
    """
    принимаем на вход строку содержащую дату и выводит в нужный формат
    """
    date = input_date[0:10]  # делаем срез
    date_replace = date.split("-")  # разбиваем по минусу
    date_revers = ".".join(date_replace[::-1])  # делаем реверс ставим точки
    return date_revers
