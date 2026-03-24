from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_details: str) -> str:
    """Принимает  номер счёта или карты, маскировка в зависимости от данных"""
    part_name = card_details.split()  # разбиваем по пробелу
    if len(part_name) < 2:
        return "Некорректный формат данных, проверьте ввод."
    if part_name[-1].isdigit():  # забираем -1 индекс и проверяем что только цифры
        number = str(part_name[-1])  # оборачиваем в целые числа
    else:
        return "Некорректный формат данных, проверьте ввод."
    initials = " ".join(part_name[:-1])  # делаем срез до - 1 индекса
    if len(part_name[-1]) == 20:  # проверка на вхождение
        masks_number = get_mask_account(number)
        return f"{initials} {masks_number}"
    elif len(part_name[-1]) == 16:
        masks_number = get_mask_card_number(number)
        return f"{initials} {masks_number}"
    else:
        return "Некорректный формат данных, проверьте ввод."


def get_date(input_date: str) -> str:
    """
    принимаем на вход строку содержащую дату и выводит в нужный формат
    """
    if len(input_date) == 0:
        return "Ошибка ввода данных"
    else:
        if not input_date[:4].isdigit():
            return "Ошибка ввода данных"
        else:
            if not input_date[5:7].isdigit():
                return "Ошибка ввода данных"
            else:
                if not input_date[8:10].isdigit():
                    return "Ошибка ввода данных"
                else:
                    year = input_date[0:4]
                    month = input_date[5:7]
                    day = input_date[8:10]

                return f"{day}.{month}.{year}"
