# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
# Подсказка: задание выполняется с помощью цикла while
my_numb = 12
user_numb = int(input('Угадайте цифру '))
while my_numb != user_numb:
    user_numb = int(input('Попробуйте снова '))
else:
    print('Поздравляю! Вы угадали!')