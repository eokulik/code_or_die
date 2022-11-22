# Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел

while True:
    try:
        a = float(input('Please enter the first number: '))
        b = float(input('Please enter the second number: '))
        print('arithmetic mean =', (a + b) / 2)
        print('geometric mean =', (a * b) ** 0.5)
        break
    except Exception as e:
        print('Wrong input format')
