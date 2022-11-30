# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’, ‘str’.
# Для каждого элемента задайте значение соответствующее названию ключа.
# Например в элемент с ключом ‘tuple’ добавьте кортеж в качестве значения.
# Содержимое этого кортежа (или что вы там добавляете)
# - на вашу фантазию, кроме строки, но количество элементов в каждом таком значении должно быть не меньше пяти.
# Т.е. если добавляете кортеж, то в нем как минимум должно быть (1, 2, 3, 4, 5),
# если список, то не меньше пяти элементов, если словарь, то не меньше пяти пар ключ-значение, итд.
# В элемент с ключом ‘str’ добавьте такую строку: “Mauris fringilla odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”
my_dict = {'tuple': (48609, True, 42, 416, 9893),
           'list': [99, 88, 77, 66, 55, False],
           'dict': {'1': 'True', '44': 'True', '90': 'True', '98939893': 'True', '41698': 'False'},
           'set': {1, 4242, False, True, 99, 66},
           'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'}
# Для того, что хранится под ключом ‘tuple’:
# выведите на экран все элементы начиная со второго и до конца
print(my_dict['tuple'][1:])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
my_dict['list'].append(12)
# удалите второй элемент списка
my_dict['list'].pop(1)
# print(my_dict['list'])

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'][('i am a tuple',)] = '25'
# print(my_dict['dict'])
# удалите какой-нибудь элемент
my_dict['dict'].pop('44')
# print(my_dict['dict'])

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
my_dict['set'].add(77)
# print(my_dict['set'])
# удалите элемент из множества
my_dict['set'].remove(4242)
# print(my_dict['set'])

# Для того, что хранится под ключом ‘str’:
# Выведите на экран из строки следующие срезы:
# первые восемь символов
print(my_dict['str'][:7])
# четыре символа из центра строки
# print(my_dict['str'])
# print((len(my_dict['str'])))
center = int(len(my_dict['str']) / 2)
# print(center)
print(my_dict['str'][(center - 2):(center + 2)])
# символы с индексами кратными трем
print(my_dict['str'][0::3])
# выведите на экран на каком месте находится слово “pretium” (делается как поиск элемента в списке)
print(my_dict['str'].find('pretium'))
# выведите на экран количество букв “l”
print(my_dict['str'].count('l'))

print(my_dict)