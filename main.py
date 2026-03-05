from src.widget import mask_account_card

card_number = "счет 1254325698567854о"  # номера карты

masked_card = mask_account_card(card_number)

print(masked_card)
