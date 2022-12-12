import random

salary = int(input('Enter your salary: '))
bonus = bool(random.getrandbits(1))


if bonus:
    salary += random.randint(1, 10000)

print(f"Your salary is ${salary}")

