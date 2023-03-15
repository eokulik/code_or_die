
class Flowers:
    def __init__(self, name, price, life_time, color, len_fl):
        self.name = name
        self.price = price
        self.life_time = life_time
        self.color = color
        self.len_fl = len_fl


class Rose(Flowers):
    def __init__(self, *args):
        super().__init__(*args)


class Lavender(Flowers):
    def __int__(self, *args):
        super().__init__(*args)


class Tulip(Flowers):
    def __init__(self, *args):
        super().__init__(*args)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def cost(self):
        return sum([f.price for f in self.flowers])

    def fresh_time(self):
        return sum([f.life_time for f in self.flowers]) / len(self.flowers)

    def sort_by_(self, param):
        return [f.name for f in sorted(self.flowers, key=lambda x: getattr(x, param))]

    def search_by_params(self, life_time_range=None, color=None, len_fl_range=None, price_range=None):
        matching_flowers = self.flowers

        if life_time_range:
            matching_flowers = [flower for flower in matching_flowers if
                                life_time_range[0] <= flower.life_time <= life_time_range[1]]

        if color:
            matching_flowers = [flower for flower in matching_flowers if flower.color == color]

        if len_fl_range:
            matching_flowers = [flower for flower in matching_flowers if
                                len_fl_range[0] <= flower.len_fl <= len_fl_range[1]]

        if price_range:
            matching_flowers = [flower for flower in matching_flowers if
                                price_range[0] <= flower.price <= price_range[1]]
        return [f.name for f in matching_flowers]


red_rose = Rose("Red Rose", 10, 20, "red", 70)
lavender = Lavender("English Lavender", 3, 30, "violet", 30)
tulip = Tulip("Parrot Tulip", 8, 15, "multi", 50)
bouquet = Bouquet([red_rose, tulip, lavender])

print(bouquet.cost())
print(bouquet.fresh_time())
print(bouquet.sort_by_('price'))
print(bouquet.sort_by_('life_time'))
print(bouquet.sort_by_('color'))
print(bouquet.sort_by_('len_fl'))
print(bouquet.search_by_params(life_time_range=(3, 25), color='red', price_range=(2, 50), len_fl_range=(2, 70)))
