import random

iterations_number = 0
random_numbers = []

while iterations_number < 15:
    random_numbers.append(random.random())
    iterations_number += 1

print("max - ", max(random_numbers))
print("min - ", min(random_numbers))
print("sum - ", sum(random_numbers))
print("avg - ", sum(random_numbers) / len(random_numbers))
