my_dict = {
    'tuple': (
        1, 2, 'text', False, 55),
    'list':
        ['asd', 434, 'djhf', 2, 3],
    'dict': {
        'key1': 'v1', 'key2': 'v2', 'key3': 'v3', 'key4': 'v4', 'key5': 'v5'},
    'set': {
        32, 'dfdf', 345, 87, 12 },
    'str':
        'Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique'
}
print(my_dict['dict'])

my_dict['list'].append('extra_value')
my_dict['list'].pop(1)
print(my_dict['list'])

my_dict['dict']['i am a tuple']= 'extra_value'
my_dict['dict'].pop('key2')
print(my_dict['dict'])

my_dict['set'] = list(my_dict['set'])
my_dict['set'].append('new_set_component')
my_dict['set'].pop(3)
my_dict['set'] = set(my_dict['set'])
print(my_dict['set'])

print(my_dict['str'][:8])

print(len(my_dict['str']) / 2)

print(my_dict['str'][43:47])

print(my_dict['str'][::3])

print(my_dict['str'].index('pretium'))

print(my_dict['str'].count('l'))

print(my_dict)