from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def get_textile_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def get_textile_consumption(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit:

    def __init__(self, height):
        self.height = height

    @property
    def get_textile_consumption(self):
        return round(2 * self.height + 0.3, 2)


class Textile:

    def __init__(self):
        self.clothes = []

    def add_clothes(self, size_or_height, type_clothes):
        if type_clothes == 'coat':
            self.clothes.append(Coat(size_or_height))
        elif type_clothes == 'suit':
            self.clothes.append(Suit(size_or_height))
        else:
            print('Данный тип одежды не поддерживается')

    @property
    def get_total_consumption(self):
        return sum([el.get_textile_consumption for el in self.clothes])


coat = Coat(10)
print(coat.get_textile_consumption)

print()
suit = Suit(10)
print(suit.get_textile_consumption)

print()
textile = Textile()
textile.add_clothes(10, 'coat')
textile.add_clothes(10, 'suit')
print(textile.get_total_consumption)
