"""
Создайте такую программу:
Программа хранит какую-либо цифру в переменной.
Программа просит пользователя угадать цифру. Пользователь вводит цифру.
Программа сравнивает цифру с той, что хранится в переменной.
Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
Т.е. программа не завершается пока пользователь не угадает цифру.
"""
from random import randint

hidden_number = randint(1, 100)
my_number = int(input('Guess the hidden number:'))
while my_number != hidden_number:
    print('Try again!')
    if my_number < hidden_number:
        print('Advice: Try entering a larger number.')
    else:
        print('Advice: Try entering a smaller number.')
    my_number = int(input('Guess the hidden number:'))
print('Good job! You are win!')
