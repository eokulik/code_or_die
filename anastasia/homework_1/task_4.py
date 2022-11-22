# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

while True:
    try:
        a = int(input('Please enter the first leg: '))
        b = int(input('Please enter the second leg: '))
        print('hypotenuse =', (a**2+b**2)**0.5)
        print('square =', (a * b)/2)
        break
    except Exception as e:
        print('Wrong input format')