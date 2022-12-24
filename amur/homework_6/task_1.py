PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def price_to_int(item):
    """
    this function transforms items
    in the list with integer prices into integer numbers
    and does not touch items without prices
    """
    if item[0].isnumeric() is True:
        value = ''
        for symbol in item:
            if symbol.isnumeric() is True:
                value += symbol
        return int(value)
    else:
        return item


def price_list_magic(info_text):
    """
    this function creates a list from the text
    and then transforms prices in it to
    integer numbers. after that it generates
    dict from the list using dict generator
    """
    info_list = list(map(price_to_int, info_text.split()))
    price_list = {info_list[i]: info_list[i + 1]
                  for i in range(0, len(info_list), 2)}
    return price_list


print(price_list_magic(PRICE_LIST))
