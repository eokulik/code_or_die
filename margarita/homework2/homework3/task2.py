import random
number = random.randint(1, 8)
while True:
    person_number = int(input("Введите загаланное число: "))
    if number == person_number:
        print('Ты правильно угадал число! Это число -', number)
    elif number > person_number:
        print('Число больше загаданного, попробуй еще раз')
    elif number < person_number:
        print('Число меньше загаданного, попробуц еще раз')
