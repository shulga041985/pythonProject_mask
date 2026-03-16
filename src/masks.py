def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты и маскирует
    """
    result = " "
    card_numbers = str(card_number)
    if len(card_numbers) == 16 and card_numbers.isdigit():
        result = f"{card_numbers[:4]} {card_numbers[4:6]}** **** {card_numbers[-4:]}"
    else:
        result = "Номер карты должен содержать 16 цифр."
    return result


def get_mask_account(mask_account: int) -> str:
    """
    Принимает на вход номер счета и маскирует
    """
    result = " "
    mask_accounts = str(mask_account)
    if not mask_accounts.isdigit():
        result = "Номер счета должен состоять из цифр."
    elif len(mask_accounts) == 4:
        result = f"**{mask_accounts}"
    elif len(mask_accounts) > 4:
        result = f"**{mask_accounts[-4:]}"
    return result
