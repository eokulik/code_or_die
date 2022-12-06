my_dict = {'tuple': (1, 2, 3, 'str', False), 'list': [1, 2, 3, 'test', True],
           'dict': {'one': 1, 'two': 2, 'Dmytrii': 'Kazban', 'four': 4, 'five': 5},
           'set': {1, 2, 3, 4, 5},
           'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'}


print(my_dict)
print(my_dict['tuple'][1:])


my_dict['list'].append('Hi:)')
my_dict['list'].pop(4)
print(my_dict['list'])


my_dict['dict']['i am a tuple'] = ('Java', 'JavaScript', 'Python')
del my_dict['dict']['Dmytrii']
print(my_dict['dict'])


my_dict['set'].add(17)
my_dict['set'].pop()
print(my_dict['set'])


print(my_dict['str'][:8])
print(my_dict['str'][8:12])
print(my_dict['str'][::3])
# my_dict['str'] = list(my_dict['str'])
print(type(my_dict['str']))
a = my_dict['str'].split()
print(a)
print(a.index('pretium'))
print(my_dict['str'].count('l'))


print(my_dict)
