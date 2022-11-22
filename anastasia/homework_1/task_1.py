# Даны 2 действительных числа a и b. Получить их сумму, разность и произведение

while True:
    try:
        a = float(input('Please enter the first number: '))
        b = float(input('Please enter the second number: '))
        print('sum =', a + b)
        print('difference =', a - b)
        print('product =', a * b)
        break
    except Exception as e:
        print('Wrong input format')