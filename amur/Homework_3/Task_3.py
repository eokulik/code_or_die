number = 0

while number < 100:
    number += 1

    if number % 3 == 0 and number % 5 != 0:
        print('Fuzz')
    elif number % 3 != 0 and number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
    else:
        print(number)
