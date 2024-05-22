data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def summator(element):
    if isinstance(element, (int, float)):
        return element # возврат целого или дробного числа
    elif isinstance(element, str):
        return len(element) # возврат длины строки
    elif isinstance(element, dict):
        return sum(len(key) for key in element) + sum(summator(value) for value in element.values()) # возврат элементов словаря
    elif isinstance(element, (list, tuple, set)):
        return sum(summator(part_of_element) for part_of_element in element) # рекурсивный подсчет элементов в списке/словаре/множестве
    else:
        return 0

print(summator(data_structure))