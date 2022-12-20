import math


def transform_value_to_int(value):
    """
    This function transforms value to integer
    and if fails sends a message and finishes the program
    """
    try:
        value = int(value)
        return value
    except ValueError:
        print('Please, enter integer number!')
        quit()


def simple_calculator():
    """
    This function calculates addition,
    subtraction, multiplication and division of numbers
    """
    print('Choose operation:', '1. Addition', '2. Subtraction',
          '3. Multiplication', '4. Division', sep='\n')
    user_variant = input('Enter the menu item number: ')
    first_number = input('Enter the first number: ')
    first_number = transform_value_to_int(first_number)
    second_number = input('Enter the second number: ')
    second_number = transform_value_to_int(second_number)
    result = False
    if user_variant == '1':
        result = f'Addition of your values is ' \
                 f'{first_number + second_number}.'
    elif user_variant == '2':
        result = f'Subtraction of your values is ' \
                 f'{first_number - second_number}.'
    elif user_variant == '3':
        result = f'Multiplication of your values is ' \
                 f'{first_number * second_number}.'
    elif user_variant == '4':
        if second_number != 0:
            quotient = math.trunc(first_number / second_number)
            result = f'Quotient after division is ' \
                     f'{quotient}. ' \
                     f'The remainder after division is ' \
                     f'{first_number - (quotient * second_number)}.'
        else:
            print('No way to divide to 0!')
            quit()
    else:
        print('Please, enter one of the variants from menu!')
    if result is not False:
        print(result)


simple_calculator()
