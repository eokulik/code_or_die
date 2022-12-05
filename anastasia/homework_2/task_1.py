# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’, ‘str’.
my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': '', 'str': ''}

# Для каждого элемента задайте значение соответствующее названию ключа.
my_dict['tuple'] = ('aaa', 111, True, 'qwerty', 222)

my_dict['list'] = ['aaa', 111, True, 'qwerty', 222]

my_dict['dict'] = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}

my_dict['set'] = set('q1w2e')

my_dict['str'] = 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'

# Для того, что хранится под ключом ‘tuple’: выведите на экран все элементы начиная со второго и до конца
print(my_dict['tuple'][1:])

# Для того, что хранится под ключом ‘list’: добавьте в конец списка еще один элемент
my_dict['list'].append(False)

# удалите второй элемент списка
# but if you mean "delete element with index 2" the function will be my_dict['list'].pop(2)
my_dict['list'].pop(1)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict']['i am a tuple'] = 6

# удалите какой-нибудь элемент
my_dict['dict'].pop('b')

# Для того, что хранится под ключом ‘set’: добавьте новый элемент в множество
my_dict['set'].add(True)

# удалите элемент из множества
my_dict['set'].remove('w')

# Для того, что хранится под ключом ‘str’:
# Выведите на экран из строки следующие срезы:
# первые восемь символов
print(my_dict['str'][:7])

# четыре символа из центра строки
middle_of_str = int(len(my_dict['str']) / 2)
print(my_dict['str'][middle_of_str - 1], my_dict['str'][middle_of_str], my_dict['str'][middle_of_str + 1],
      my_dict['str'][middle_of_str + 2])

# символы с индексами кратными трем
print(my_dict['str'][3::3])

# выведите на экран на каком месте находится слово “pretium” (делается как поиск элемента в списке)
words = my_dict['str'].split()
for word in words:
    if word == 'pretium':
        print(words.index(word))

# выведите на экран количество букв “l”
l_number = my_dict['str'].count('l')
print(l_number)

# В конце выведите на экран весь словарь
print(my_dict)
