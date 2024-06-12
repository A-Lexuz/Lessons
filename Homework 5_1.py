class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        current_floor = 1
        print (f"Вы на {current_floor} этаже здания {self.name}")
        while new_floor >= current_floor:
            current_floor += 1
            if current_floor == self.number_of_floors:
                print(f"Вы на последнем ({current_floor}) этаже здания {self.name}")
            elif current_floor < self.number_of_floors:
                print(f"Вы на {current_floor} этаже здания {self.name}")
            elif current_floor > self.number_of_floors:
                print(f'Больше этажей в здании {self.name} нет')
                break
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(4)