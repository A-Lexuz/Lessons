def personal_sum(numbers):   #создаём функцию подсчёта суммы чисел, а также корректного и не корректного ввода
    result = 0  # создаём переменную для подсчёта суммы
    incorrect_data = 0 # создаём переменную для посчёта ошибок
    correct_data = 0  # создаём переменную для подсчета верных значений
    for number in numbers: # создаём цикл для перебора каждого значения
        try:
            result += number
            correct_data += 1
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}') # перехват ошибок неверного ввода
            incorrect_data += 1
    return (result, incorrect_data, correct_data) # возвращаем подсчёт суммы чисел, ошибки, верные значения

def calculate_average(numbers): # создаём функцию для подсчёта среднего значения
    try:
        average = personal_sum(numbers)  # передаём кортеж для дальнейшей работы функции
        return average[0] / average[2]   # делим сумму от функции personal_sum на количество верных значений
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В {numbers} записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
