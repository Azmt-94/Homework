class House:
    houses_history = []

    def __new__(cls, *args):
        instance = super().__new__(cls)
        instance.__init__(*args)
        cls.houses_history.append(args[0])
        cls.name = args[0]
        cls.number_of_floors = args[1]
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
