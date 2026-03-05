from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_number: str) -> str:
    """Принимает  номер счёта или карты, маскировка в зависимости от данных"""

    part_name = card_number.split()
    if part_name[-1].isdigit():
        number = int(part_name[-1])
    else:
        return "Номер не состоит из цифр, введите корректный номер"
    initials = " ".join(part_name[:-1])
    if initials.upper() == "СЧЕТ":
        masks_number = get_mask_account(number)
    else:
        masks_number = get_mask_card_number(number)
    return f"{initials} {masks_number}"
