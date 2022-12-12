from random import random
numbers_list = []
while len(numbers_list) < 15:
    numbers_list.append(random())
print(max(numbers_list), '- Максимальное число')
print(min(numbers_list), '- Минимальное число')
print(sum(numbers_list), '- Сумма всех чисел')
print(sum(numbers_list) / len(numbers_list), '- Среднее арифметическое чисел')
