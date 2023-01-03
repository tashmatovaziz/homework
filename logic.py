import random


def bet(number, amount):
    win_number = random.randint(1, 31)
    if number == win_number:
        print(f'Вы выиграли {amount * 2}')
        return amount * 2
    else:
        print(f'Вы проиграли {-amount}')
        return -amount