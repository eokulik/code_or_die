PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def price_int():
    mid_text = []
    result = list(PRICE_LIST.split())
    for word in result:
        if word.endswith('р'):
            word = word.replace('р', ';')
        else:
            word = word + ' -'
        mid_text.append(word)
        fin_text = ' '.join(mid_text)
    for word in fin_text:
        if word.endswith(';'):
            word = word.replace(';', '.')
        mid_text.append(word)
        final_text = ' '.join(mid_text)

    print(final_text)

price_int()