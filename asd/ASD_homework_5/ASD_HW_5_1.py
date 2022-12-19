import math

def calc():
    operation = int(input('''
Пожалуйста, выберите желаемую операцию:
1.Сложение
2.Вычитание
3.Умножение
4.Деление
и введите номер пункта меню 
'''))
    numb1 = float(input('Введите первое число: '))
    numb2 = float(input('Введите второе число: '))

    if operation not in range(1, 5):
        print("Неправильный оператор, попробуйте снова")
        again()

    else:

        print('''
Ваш результат: ''')
        if operation == 1:
            print('{} + {} = '.format(numb1, numb2))
            print(numb1 + numb2)
        elif operation == 2:
            print('{} - {} = '.format(numb1, numb2))
            print(numb1 - numb2)
        elif operation == 3:
            print('{} * {} = '.format(numb1, numb2))
            print(numb1 * numb2)
        elif operation == 4:
            if numb2 !=0:
                print("Частное: ", int(numb1 // numb2))
                print("Остаток: ", int(numb1 % numb2))
            else:
                print("Деление на ноль!")


def again():
    calc_again = input('''
Хотите попробовать снова?
Если да, введите  +  и если нет то  - .
''')

    if calc_again.upper() == '+':
        calc()
    elif calc_again.upper() == '-':
        print('До встречи')
    else:
        again()


calc()
while 1 == 1:
    again()
