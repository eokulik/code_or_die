my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [1, 2, 3, 4, 5],
           'dict': {'one': 'cat', 'two': 'dog', 'three': 'bird', 'four': 'fish', 'five': 'cow'},
           'set': {1, 2, 3, 4, 5},
           'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'}

# printed element 'tuple'
print(my_dict['tuple'])

# tasks with element 'list'
my_dict['list'].append(8)
my_dict['list'].pop(1)

# tasks with element 'dict'
my_dict['dict'][('i am a tuple',)] = 'wow'
my_dict['dict'].pop('one')

# tasks with element 'set'
my_dict['set'].add(9)
my_dict['set'].remove(5)

# tasks with element 'str'
s = my_dict.get('str')
print(s[:8])
length = round(len(s) / 2 - 2)  # found the middle of the line minus 2 and rounded the number
print(s[length:length + 4])
print(s[::3])
print(s.find('pretium'))
print(s.count('l'))

# printed all dictionary
print(my_dict)
