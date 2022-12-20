number = 0

while number < 100:
    number += 1
    if number % 5 == 0 and number % 3 == 0:
        print('FuzzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fuzz')
    else:
        print(number)
