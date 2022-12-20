number = 11

entered_number = int(input('Попробуйте угадать цифру '))

while number != entered_number:
    entered_number = int(input('попробуйте снова '))
else:
    print('Поздравляю!Вы угадали!')
