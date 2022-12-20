# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
# После этого выведите на экран максимальное из сгенеренных рандомов,
# минимальное, сумму всех рандомов и их среднее арифметическое.

from random import random

random_numbers = []

while len(random_numbers) < 15:
    random_numbers.append(random())
print('max -', max(random_numbers))
print('min -', min(random_numbers))
print('sum -', sum(random_numbers))
print('avg -', sum(random_numbers) / len(random_numbers))
