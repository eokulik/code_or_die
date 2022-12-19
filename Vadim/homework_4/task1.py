# Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.


import random

salary = int(input('Enter your salary = '))
bonus = bool(random.getrandbits(1))

if bonus:
    salary = salary + random.randint(1, 5000)

print(f"Salary with bonus = ${salary}")
