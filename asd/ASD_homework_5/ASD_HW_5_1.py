def calc(numb1, numb2, operation):
    if operation == 1:
        print('''
        Ваш результат: ''')
        print('{0} + {1} = '.format(numb1, numb2))
        print(numb1 + numb2)
    elif operation == 2:
        print('''
        Ваш результат: ''')
        print('{0} - {1} = '.format(numb1, numb2))
        print(numb1 - numb2)
    elif operation == 3:
        print('''
        Ваш результат: ''')
        print('{0} * {1} = '.format(numb1, numb2))
        print(numb1 * numb2)
    elif operation == 4:
        if numb2 != 0:
            print('''
            Ваш результат: ''')
            print("Частное: ", int(numb1 // numb2))
            print("Остаток: ", int(numb1 % numb2))
        else:
            print("Деление на ноль!")


def operation():
    operation = int(input('''
    Пожалуйста, выберите желаемую операцию:
    1.Сложение
    2.Вычитание
    3.Умножение
    4.Деление
    и введите номер пункта меню
    '''))
    if operation not in range(1, 5):
        print("Неправильный оператор")
    else:
        numb1 = float(input('Введите первое число: '))
        numb2 = float(input('Введите второе число: '))
        calc(numb1, numb2, operation)


def again():
    calc_again = input('''
Хотите попробовать снова?
Если да, введите  +  и если нет то  - .
''')
    if calc_again.upper() == '+':
        operation()
    elif calc_again.upper() == '-':
        print('До встречи')
        exit()


operation()

while True:
    again()


