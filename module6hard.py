class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides, filled=False):
        self.__sides = list(__sides)
        self.__color = list(__color)
        self.__filled = filled

    # {(255, 0, 0): 'Red', (0, 255, 0): 'Lime', (0, 0, 255): 'Blue', (255, 255, 255): 'White', (0, 0, 0): 'Black',
    #  (128, 128, 128): 'Gray', (255, 0, 255): 'Pink', (255, 255, 0): 'Yellow', (0, 255, 255): 'Aqua',
    #  (192, 192, 192): 'Silver', (128, 0, 0): 'Maroon', (128, 128, 0): 'Olive', (0, 128, 0): 'Green',
    #  (0, 128, 128): 'Teal', (0, 0, 128): 'Navy', (128, 0, 128): 'Purple'}

    def get_color(self):
        return self.__color

    def __is_valid_color(self, red, green, blue):
        if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
            return True
        else:
            return False

    def set_color(self, red, green, blue):
        if self.__is_valid_color(red, green, blue) is True:
            self.__color = [red, green, blue]

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides) is True:
            self.__sides = list(sides)

    def __is_valid_sides(self, *sides):
        if len(sides) != self.sides_count:
            return False
        else:
            for i in sides:
                if i <= 0:
                    return False
                else:
                    return True

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        if len(__sides) != self.sides_count:
            __sides = [1]
            super().__init__(__color, *__sides)
        else:
            super().__init__(__color, *__sides)
        self.__radius = sum(self.get_sides()) / 2 / 3.14

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return self.__radius ** 2 * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        if len(__sides) != self.sides_count:
            __sides = [1, 1, 1]
            super().__init__(__color, *__sides)
        else:
            super().__init__(__color, *__sides)
        self.__height = ((self.__len__() / 2 * (self.__len__() / 2 - self.get_sides()[0]) *
                          (self.__len__() / 2 - self.get_sides()[1]) *
                          (self.__len__() / 2 - self.get_sides()[2])) ** 0.5) / self.get_sides()[1] * 2

    def get_square(self):
        return self.__height * self.get_sides()[1] / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, *__sides):
        if len(__sides) != 1:
            __sides = [1] * 12
            super().__init__(__color, *__sides)
        else:
            __sides = [*__sides] * 12
            super().__init__(__color, *__sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


# figure1 = Figure((155, 155, 155), 12)
# print(figure1.get_color())
# figure1.set_color(55, 66, 77) # Изменится
# print(figure1.get_color())
# figure1.set_color(300, 70, 15) # Не изменится
# print(figure1.get_color())
#
# print(figure1.get_sides())
# figure1.set_sides(34)
# print(figure1.get_sides())
# figure1.set_sides(12, 20)
# print(figure1.get_sides())
# figure1.set_sides(-12, 20)
# print(figure1.get_sides())
# print(figure1.__len__())
# circle1 = Circle((155,200,155), 13)
# print(circle1.get_color())
# print(circle1.get_sides())
# print(circle1.__len__())
# print(circle1.get_radius())
# print(circle1.get_square())
# trian1 = Triangle((155,155,155), 3,4)
# print(trian1.get_color())
# print(trian1.get_sides())
# print(trian1.get_square())
# cube1 = Cube((155,155,155),12,12)
# print(cube1.get_sides())
# print(cube1.get_volume())

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
