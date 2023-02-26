operation = input('Выберите операцию(+,-, *, /): ')
first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))


def calculator():
    if operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '*':
        print(first_number * second_number)
    elif operation == '/':
        if second_number != 0:
            print(first_number / second_number)
        else:
            print('На ноль делить нельзя')


calculator()
