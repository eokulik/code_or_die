PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def price_int():
    middle_text = []
    result = list(PRICE_LIST.split())
    for word in result:
        if word.endswith('р'):
            word = word.replace('р', ' ')
        else:
            word = word + ' -'
        middle_text.append(word)
        final_text = ' '.join(middle_text)
    my_gen(final_text)


def my_gen(final_text):
    result = dict((a.strip(), int(b.strip()))
                  for a, b in (element.split('-')
                               for element in final_text.split('  ')))
    print(result)


price_int()
