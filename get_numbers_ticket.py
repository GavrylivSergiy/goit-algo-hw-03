import random
def get_numbers_ticket(min_num, max_num, quantity):
    
    if quantity > (max_num - min_num + 1):
        raise ValueError()
    numbers = set()
    while len(numbers) < quantity:

        numbers.add(random.randint(min_num, max_num))
    
    return sorted(list(numbers))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)