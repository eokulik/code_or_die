import math

my_dict = {'tuple': '', 'list': '', 'dict':'', 'set': '', 'str': ''}

my_dict['tuple'] = ('text', 123, False, 234, 345)
my_dict['list'] = ['text1', 223, True, 233, 243]
my_dict['dict'] = {'a1': 111, 'a2': 222, 'a3': 'True', 'a4': 'True', 'a5': 333}
my_dict['set'] = {11, 22, 33, 44, 55}
my_dict['str'] = 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'


print(my_dict['tuple'][1:])

my_dict['list'].append('Vadim')

my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 1

my_dict['dict'].pop('a1')

my_dict['set'].add(66)

my_dict['set'].remove(11)

print(my_dict['str'][:8])

mid_symb_str = math.ceil(len(my_dict['str']) / 2)
print('Middle symbols = ', my_dict['str'][(mid_symb_str - 2):(mid_symb_str + 2)])

print(my_dict['str'][::3])

print(my_dict['str'].find('pretium'))

print(my_dict['str'].count('l'))

print(my_dict)
