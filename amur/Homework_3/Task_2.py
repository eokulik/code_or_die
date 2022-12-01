number = 9
while True:
    user_number = input('Guess the number: ')
    for symbol in user_number:
        if symbol.isdigit() is False:
            print('Please, enter an integer number!')
            break
    if number == int(user_number):
        print('Congratulations! You guessed it!')
        break
    else:
        print('Please, try again!')
