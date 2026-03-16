def filter_by_state(date_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению.
    """
    generated_list = []  # создаем пустой список
    for item in date_list:  # перебераем прилетевший список
        if item.get("state") == state:  # проверяем зависимость ключа к условию
            generated_list.append(item)  # добавляем словарь в список
    return generated_list


def sort_by_date(date_list: list[dict], date: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция возвращает новый список, отсортированный по дате (date).
    """

    sorted_date = sorted(date_list, key=lambda x: x["date"], reverse=date)  # сортируем через лямбду по ключу date
    return sorted_date
