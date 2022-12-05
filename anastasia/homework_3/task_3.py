# Напишите программу, которая перебирает последовательность от 1 до 100.
# Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа, а для чисел кратных 5 печатать "Buzz".
# Для чисел которые кратны одновременно и 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.
#
# Вывод должен быть следующим:
# 1
# 2
# fuzz
# 4
# buzz
# fuzz
# 7
# 8
# ..
# 14
# FuzzBuzz
# 16
# ...
#
# Подсказка: При тестировании своей программы обращайте внимание на числа 3, 5 и 15
# (точнее на то, что должно быть напечатано вместо них)

i = 0

while i < 100:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fuzz')
    else:
        print(i)
