class Flowers:
    material = 'plant'

    def __init__(self, freshness: bool, stem_length: int,
                 colour: str, price: int, life: int):
        self.freshness = freshness
        self.stem_length = stem_length
        self.colour = colour
        self.price = price
        self.life = life


class FieldFlowers(Flowers):
    def __init__(self, freshness, stem_length, colour, life, price=0):
        super().__init__(freshness, stem_length, colour, price, life)


class ShopFlowers(Flowers):
    def __init__(self, freshness, stem_length, colour, price, life=48):
        super().__init__(freshness, stem_length, colour, price, life)


class Bouquet:
    def __init__(self):
        self.rose = ShopFlowers(True, 20, 'red', 20)
        self.chamomile = FieldFlowers(False, 2, 'yellow', 300)
        self.tulip = ShopFlowers(False, 19, 'yellow', 23, 60)
        self.sunflower = FieldFlowers(True, 100, 'green and yellow', 333, 15)

    def time_to_die(self):
        die_time = (
            self.rose.life + self.chamomile.life
            + self.tulip.life + self.sunflower.life) / 4
        return f'Average time of bouquet dying is {die_time}'

    def total_price(self):
        total_price = (
            self.rose.price + self.chamomile.price
            + self.tulip.price + self.sunflower.price)
        return f'Total price is {total_price}'

    def sort_by_param(self, param):
        name_and_value = {
            'rose': self.rose.__getattribute__(param),
            'chamomile': self.chamomile.__getattribute__(param),
            'tulip': self.tulip.__getattribute__(param),
            'sunflower': self.sunflower.__getattribute__(param)}
        names = sorted(name_and_value, key=name_and_value.__getitem__)
        return f'Without sorting - {name_and_value}.' \
               f' Sort by {param}: {names}'

    def search_by_param(self, param, query):
        result = {}
        name_and_value = {
            'rose': self.rose.__getattribute__(param),
            'chamomile': self.chamomile.__getattribute__(param),
            'tulip': self.tulip.__getattribute__(param),
            'sunflower': self.sunflower.__getattribute__(param)}
        for key, value in name_and_value.items():
            if value == query:
                result[key] = value
        return f'Search by {query} in {param}. Result - {result}'


my_bouquet = Bouquet()
print(my_bouquet.time_to_die())
print(my_bouquet.total_price())
print(my_bouquet.sort_by_param('colour'))
print(my_bouquet.sort_by_param('price'))
print(my_bouquet.sort_by_param('life'))
print(my_bouquet.sort_by_param('stem_length'))
print(my_bouquet.sort_by_param('freshness'))
print(my_bouquet.search_by_param('colour', 'yellow'))
print(my_bouquet.search_by_param('life', 48))
print(my_bouquet.search_by_param('life', 4))
print(my_bouquet.search_by_param('freshness', True))
