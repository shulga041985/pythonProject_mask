from src.masks import get_mask_account, get_mask_card_number

card_number = 1254325698567854  # номера карты
account_number = 895218469522852445  # номера счета

masked_card = get_mask_card_number(card_number)
masked_account = get_mask_account(account_number)

print(f"Маскированный номер карты: {masked_card}")
print(f"Маскированный номер счета: {masked_account}")
