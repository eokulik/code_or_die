"""
Напишите программу, которая перебирает последовательность от 1 до 100.
Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz".
Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.
"""
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for number in numbers_list:
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
        continue
    elif number % 3 == 0:
        print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
