# Выполните random.random() 15 раз, сохраняя куда-то каждый результат.
# После этого выведите на экран максимальное из сгенеренных рандомов,
# минимальное, сумму всех рандомов и их среднее арифметическое.

import random

my_list = []
range_a = range(1, 16)
for i in range_a:
    my_list.append(random.random())
print('Максимальное значение:', max(my_list))
print('Минимальное значение:', min(my_list))
print('Сумма значений:', sum(my_list))
print('Среднее арифметическое значений:', sum(my_list) / max(range_a))
