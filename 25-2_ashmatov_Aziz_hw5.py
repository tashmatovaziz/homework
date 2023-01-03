import log
from decouple import config
MY_MONEY = config('MY_MONEY', cast=int)

while True:
    user_answer = input('хотите ли вы сыграть еще(да или нет): ')
    if user_answer == 'нет':
        break
    elif user_answer != 'нет' and user_answer != 'да':
        continue
    user_slot = int(input('введите число от 1 до 30: '))
    user_sum = int(input('ставте деньги: '))
    log.lor(user_answer, user_sum, user_slot)

print(f'хорошего дня!!!')