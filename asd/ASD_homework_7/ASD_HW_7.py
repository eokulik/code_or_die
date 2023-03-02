first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))


def my_dec(func):
    def wrapper(numb1, numb2):
        if numb1 < 0 or numb2 < 0:
            operation = 3
        elif numb1 == numb2:
            operation = 1
        elif numb1 > numb2:
            operation = 2
        elif numb1 < numb2:
            operation = 4
        func(numb1, numb2, operation)
    # print(wrapper(first_number, second_number, operation))
    return wrapper


@my_dec
def calc(numb1, numb2, operation):
    if operation == 1:
        print('''
        Ваш результат: ''')
        print('{0} + {1} = '.format(numb1, numb2))
        print(numb1 + numb2)
    elif operation == 2:
        print('''
        Ваш результат: ''')
        print('{1} - {0} = '.format(numb1, numb2))
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


calc(first_number, second_number)
