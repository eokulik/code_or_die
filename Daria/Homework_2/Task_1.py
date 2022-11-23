'''Создание словаря
Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’, ‘str’.
Для каждого элемента задайте значение соответствующее названию ключа. Например в элемент с ключом ‘tuple’ добавьте кортеж в качестве значения. Содержимое этого кортежа (или что вы там добавляете) - на вашу фантазию, кроме строки, но количество элементов в каждом таком значении должно быть не меньше пяти. Т.е. если добавляете кортеж, то в нем как минимум должно быть (1, 2, 3, 4, 5), если список, то не меньше пяти элементов, если словарь, то не меньше пяти пар ключ-значение, итд.
В элемент с ключом ‘str’ добавьте такую строку: “Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique”

Действия с элементами словаря my_dict:
Для того, что хранится под ключом ‘tuple’:
выведите на экран все элементы начиная с первого и до конца

Для того, что хранится под ключом ‘list’:
добавьте в конец списка еще один элемент
удалите второй элемент списка

Для того, что хранится под ключом ‘dict’:
добавьте элемент с ключом ('i am a tuple',) и любым значением
удалите какой-нибудь элемент

Для того, что хранится под ключом ‘set’:
добавьте новый элемент в множество
удалите элемент из множества

Для того, что хранится под ключом ‘str’:
Выведите на экран из строки следующие срезы:

первые восемь символов
четыре символа из центра строки
символы с индексами кратными трем
выведите на экран на каком месте находится слово “pretium” (делается как поиск элемента в списке)
выведите на экран количество букв “l”
В конце выведите на экран весь словарь'''

my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [1, 2, 3, 4, 5],
           'dict': {'one': 'cat', 'two': 'dog', 'three': 'bird', 'four': 'fish', 'five': 'cow'},
           'set': set((1, 2, 3, 4, 5)),
           'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'}

# printed element 'tuple'
print(my_dict['tuple'])

# tasks with element 'list'
my_dict['list'].append(8)
my_dict['list'].pop(1)

# tasks with element 'dict'
my_dict['dict']['i am a tuple'] = 'wow'
my_dict['dict'].pop('one')

# tasks with element 'set'
my_dict['set'].add(9)
my_dict['set'].remove(5)

# tasks with element 'str'
s = my_dict.get('str')
print(s[:8])
l = round(len(s) / 2 - 2)  # found the middle of the line minus 2 and rounded the number
print(s[l:l + 4])
print(s[::3])
print(s.find('pretium'))
print(s.count('l'))

# printed all dictionary
print(my_dict)

