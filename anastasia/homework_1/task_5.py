# Программа запрашивает у пользователя длину ребра куба. И находит объем куба и площадь его боковой поверхности

while True:
    try:
        a = int(input('Please enter the cube edge length : '))
        print('volume =', a ** 3)
        print('lateral surface area =', 4 * a ** 2)
        break
    except Exception as e:
        print('Wrong input format')
