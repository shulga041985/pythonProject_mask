from src.widget import mask_account_card, get_date

card_details = "счет 1254325698567854"  # номера карты или счета
masked_card = mask_account_card(card_details)

print(masked_card)

input_date = "2024-03-11T02:26:18.671407"  # входной формат даты
correct_date = get_date(input_date)

print(correct_date)
