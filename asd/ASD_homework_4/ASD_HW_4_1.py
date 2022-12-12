# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'
import random
import sys
salary = int(input('Input salary $ '))
bonus = bool(random.getrandbits(1))
bonus_add = int(random.randint(0, sys.maxsize))
if bonus is True:
    print('$', (salary + bonus_add))
else:
    print('$', salary)
