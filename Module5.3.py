class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __add__(self, other):
        if isinstance(other, House):
            return self.number_of_floors + other.number_of_floors
        if isinstance(other, int):
            return self.number_of_floors + other

    def __radd__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value

    def __iadd__(self, value):
        return self.__add__(value)
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
