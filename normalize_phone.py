import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    normalized_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Додаємо міжнародний код, якщо його немає
    if not normalized_number.startswith('+'):
        normalized_number = '+38' + normalized_number
    
    return normalized_number

# Приклад використання
phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

for number in phone_numbers:
    print(normalize_phone(number))