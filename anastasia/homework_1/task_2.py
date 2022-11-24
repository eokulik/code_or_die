# Даны действительные числа x и y. Получить x − y / 1 + xy

while True:
    try:
        x = float(input('Please enter x value: '))
        y = float(input('Please enter y value: '))
        print('x - y / 1 + xy =', (x - y) / (1 + x * y))

    except Exception:
        print('Wrong input format')
