import math

my_dict = {
    'tuple': ('some_random_text', True, 4, 'hello', (1, 2)),
    'list': [1, 2, False, 'Hello', 'Hey'],
    'dict': {'v1': 1, 'v2': 2, 'v3': 3, 'v4': 4, 'v5': 'Today'},
    'set': {'hello everybody', 1, 2, 5, 'hey'},
    'str': 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}

print(my_dict['tuple'][1:])

my_dict['list'].append('extra element')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 'puppy'
my_dict['dict'].pop('v1')

my_dict['set'].add('11')
my_dict['set'].pop()
print(my_dict['set'])

print('First 8 symbols -', my_dict['str'][:8])
cntr_of_str = math.ceil(len(my_dict['str'])/2)
print('Symbols from center -', my_dict['str'][(cntr_of_str-2):(cntr_of_str+2)])
print('Characters with indexes multiple to 3 -', my_dict['str'][::3])
print('Where is "pretium" -', my_dict['str'].index('pretium'))
print('Number of "l" letters -', my_dict['str'].count('l'))

print(my_dict)
