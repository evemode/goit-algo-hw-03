import random

def get_numbers_ticket(min_num:int, max_num:int, quantity:int) -> list[int]:
    '''choosing random numbers according to given parameters'''
    if 0 < min_num and max_num <=1000: #checks conditions
        chosen_numbers = sorted(random.sample(range(min_num, max_num), quantity)) #choosing random unique numbers and sorting them
        return chosen_numbers
    return []

lottery_numbers = get_numbers_ticket(1, 1000, 6)
print("Ваші лотерейні числа:", lottery_numbers)