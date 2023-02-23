
first = float(input('Введите первое число: '))

second = float(input('Введите второе число: '))

operation = []


def my_dec(func):
    def wrapper(first, second):
        if first == second:
            return first + second
        elif first < 0 or second < 0:
            return first * second
        elif first > second:
            return second - first
        elif first < second:
            return first / second
        func(first, second, operation)
    print(wrapper(first, second))
    return wrapper


@my_dec
def calc(first, second, operation):
    if operation == 1:
        return first + second


calc(first, second)
