# Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
# Спросите у пользователя salary. А bonus пусть назначается рандомом.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

from random import randint

salary = int(input('Please enter your salary: '))
bonus = bool(randint(0, 1))

if bonus is True:
    salary_with_bonus = salary + randint(1, 1000)
else:
    salary_with_bonus = salary
print(str(salary) + ',', bonus, '- \'$' + str(salary_with_bonus) + '\'')
