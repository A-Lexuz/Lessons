my_list = ['Apple', 'Banana', 'Peach', 'Pear', 'Pineapple', 'Orange']
print('Список продуктов:', my_list)
print('Первый и последний продукт:', my_list[0], ',', my_list[-1])
print('С третьего по пятый продукт',my_list[2:4]) # Вывод значений из списка с 3 по 5 элемент, не включая последний, если не включая, то print(my_list[2:5])
my_list[2] = 'Apricot'
print('Новый список продуктов:', my_list)
print('')
my_dict = {'Apple':'Яблоко', 'Banana':'Банан', 'Peach':'Персик', 'Pear':'Груша', 'Pineapple':'Ананас', 'Orange':'Апельсин'}
print('Словарь:', my_dict)
print('Перевод слова "Orange":', my_dict['Orange'])
my_dict['Orange'] = 'Оранжевый'
print("Новая версия словаря:", my_dict)
