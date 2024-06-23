
class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Black', 'White', 'Grey']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        print('Модель:', self.__model)

    def get_horsepower(self):
        print('Мощность двигателя:', self.__engine_power)

    def get_color(self):
        print('Цвет:', self.__color)

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print("Владелец:", self.owner)

    def set_color(self, new_color):
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на", new_color)


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
print(' ')
vehicle1.print_info()