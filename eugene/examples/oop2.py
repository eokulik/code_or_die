class Cat:
    def __init__(self) -> None:
        self.__pows = 4
        self.__tail = True
        self._ears = 2
        self.__fur = True

    @property
    def pows(self):
        return self.__pows

    @pows.setter
    def pows(self, pows_qty):
        self.__pows = pows_qty

    @pows.deleter
    def pows(self):
        del self.__pows

barsik = Cat()
barsik.pows = 5
# del barsik.pows
print(barsik.pows)