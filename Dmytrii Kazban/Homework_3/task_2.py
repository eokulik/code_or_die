# Задание №2 - "Угадайка"
# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
#
# Подсказка: задание выполняется с помощью цикла while

number_to_guess = 8
number_to_enter = int(input("Enter the number"))


while number_to_enter != number_to_guess:
    if number_to_enter != number_to_guess:
        print("Try another number")
        number_to_enter = int(input("Enter the number"))
else:
        print("Congrats! You've guessed the number")
