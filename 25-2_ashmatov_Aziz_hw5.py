from logic import bet
from decouple import config

money = config('MY_MONEY')

while True:
    answer = input(f'Будете играть? (остаток:{money}) ')
    if answer.lower() == 'да':
        number = input('Число на которое хотите поставить: ')
        if not number.isnumeric():
            print('Число должно быть только из цифр')
        number = int(number)
        if number < 1 or number > 30:
            print('Число должно быть от 1 до 30 включительно')
        amount = input('Сколько хотите поставить: ')
        if not amount.isnumeric():
            print('Сумма ставки должна быть целым числом')
        amount = int(amount)
        if amount < 0 or amount > money:
            print(f'сумма должна быть больше нуля и  меньше {money}')
        money += bet(number, amount)
    else:
        print(f'До свидания у вас осталось {money}')

    if money <= 0:
        print(f'у вас не осталось денег! Приходите когда будут')