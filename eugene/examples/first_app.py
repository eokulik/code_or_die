print('Hello World!')


def append_to_dict(dictonary: dict, **kwargs):
    '''
    This function appends values given in kwargs to the given dictionary
    '''
    # print(kwargs)
    for key, value in kwargs.items():
        dictonary[key] = value
    return dictonary


print(append_to_dict(1, key1='c', key2='g'))
