class Car():
    def __init__(self,model, __vin, __numbers):
        print(f'   Пытаемся создать автомобиль {model}')
        self.model = model
        if self.__is_valid_vin(__vin) == True:
            self.vin = __vin
        if self.__is_valid_numbers(__numbers) == True:
            self.numbers = __numbers

    def __is_valid_vin(self,vin_number):
        if isinstance(vin_number, int) == False:
            raise IncorrectVinNumber(f'{vin_number} - Некорректный тип vin номера, автомобиль {self.model} создать нельзя')
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber(f'{vin_number} Неверный диапазон vin номера, автомобиль {self.model} создать нельзя')
        else:
            return True

    def __is_valid_numbers(self,numbers):
        if isinstance(numbers, str) == False:
            raise IncorrectCarNumbers(f'{numbers} - Некорректный тип данных для номеров, '
                                      f'автомобиль {self.model} создать нельзя')
        elif len(numbers) != 6:
            raise IncorrectVinNumber(f'Неверная длина номера, автомобиль {self.model} создать нельзя')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  car1 = Car('Toyota Hulix', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{car1.model} успешно создан')

try:
  car2 = Car('Tesla Model X', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{car2.model} успешно создан')

try:
  car3 = Car('BMV X5', 1000000, 123456)
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{car3.model} успешно создан')

try:
  car4 = Car('Ford Focus', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{car4.model} успешно создан')

try:
  car5 = Car('Mazda CX-5', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{car5.model} успешно создан')