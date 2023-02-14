first_number = input('Enter the first number. ')
second_number = input('Enter the second number. ')

try:
    float_first_number = float(first_number)
    float_second_number = float(second_number)
except ValueError as err:
    print('Error: all the numbers should be numbers!')
    raise err


def logic(func):
    def wrapper(first, second):
        if (first >= 0 and second >= 0) and first == second:
            operation = '+'
        elif (first >= 0 and second >= 0) and first > second:
            operation = '-'
        elif (first >= 0 and second >= 0) and first < second:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        else:
            operation = 'Error'
        func(first, second, operation)
    return wrapper


@logic
def calc(first, second, operation):
    text = ''
    result = 'Error'
    if operation == '+':
        text = 'The numbers are equal, the addition of these numbers is'
        result = first + second
        if result == 0.0:
            result = 0
    elif operation == '-':
        text = 'The first is greater than the second, ' \
               'subtracting the second from the first is'
        result = first - second
        if result == 0.0:
            result = 0
    elif operation == '/':
        text = 'The second is greater than the first, ' \
               'dividing the first by the second is'
        result = first / second
        if result == 0.0:
            result = 0
    elif operation == '*':
        text = 'One of the numbers is negative, the multiplication is'
        result = first * second
        if result == -0.0:
            result = 0
    return print(text, result)


calc(float_first_number, float_second_number)
