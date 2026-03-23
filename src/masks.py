def get_mask_card_number(card_number: str) -> str:
    """
    Принимает на вход номер карты и маскирует
    """
    result = " "
    card_numbers = card_number.replace(" ", "").replace("-", "")
    if len(card_numbers) == 16 and card_numbers.isdigit():
        result = f"{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}"
    else:
        result = 'Не корректный ввод номера карты.'
    return result


def get_mask_account(mask_account: str) -> str:
    """
    Принимает на вход номер счета и маскирует
    """
    result = " "
    mask_accounts = mask_account.replace(" ", "").replace("-", "")
    if not mask_accounts.isdigit():
        result = "Номер счета должен состоять из цифр."
    elif len(mask_accounts) == 4:
        result = f"**{mask_accounts}"
    elif len(mask_accounts) > 4:
        result = f"**{mask_accounts[-4:]}"
    return result
