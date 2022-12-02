import math

number = 0

while number < 100:
    number += 1
    num_3 = number / 3
    num_5 = number / 5

    if num_3 == math.ceil(num_3) and num_5 != math.ceil(num_5):
        print('Fuzz')
    elif num_3 != math.ceil(num_3) and num_5 == math.ceil(num_5):
        print('Buzz')
    elif num_3 == math.ceil(num_3) and num_5 == math.ceil(num_5):
        print('FuzzBuzz')
    else:
        print(number)
