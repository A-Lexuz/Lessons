class Animal:
    alive = True  # Живой
    fed = False  # Накормленный

    def __init__(self, name):
        self.name = name  # индивидуальное назнвание животных

    def eat(self, food):
        if food.edible is True:
            print(self.name, "съел ", food.name)
            self.fed = True
        else:
            print(self.name, 'не стал есть', food.name)
            self.alive = False

class Plant:
    edible = False  # Съедобность

    def __init__(self, name):
        self.name = name  # индивидуальное название растений


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)