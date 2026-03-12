def filter_by_state(data_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и выводит
    в зависимости от значения ключа state выбраный список словарей
    """
    mi_list = []  # создаем пустой список
    for item in data_list:  # перебераем прилетевший список
        if item.get("state") == state:  # проверяем зависимость ключа к условию
            mi_list.append(item)  # добавляем словарь в список
    return mi_list


def sort_by_date(list_date: list[dict], date: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    и возвращает новый список, отсортированный по дате"""

    sorted_date = sorted(list_date, key=lambda x: x["date"], reverse=date)
    return sorted_date
