# словарь words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
# Выведите на экран каждый ключ столько раз сколько указано в значении.

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, key in words.items():
    print(word * key)
