import random

numbers_list = list()

for i in range(15):
    numbers_list.append(random.random())

print(max(numbers_list))
print(min(numbers_list))
print(sum(numbers_list))
print(sum(numbers_list) / len(numbers_list))
