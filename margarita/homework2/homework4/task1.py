from random import randint
salary = int(input('Введите размер заработной платы: '))
bonus = bool(randint(0, 1))
if bonus is True:
    print(salary, ',', bonus, '-', salary + bonus)
else:
    print(salary, ',', bonus, '-', salary)
