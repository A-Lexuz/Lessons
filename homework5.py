my_list = ['Apple', 'Banana', 'Peach', 'Pear', 'Pineapple', 'Orange']
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5]) # Вывод значений из списка с 3 по 5 элемент включительно, если не включая, то print(my_list[2:4])
my_list[2] = 'Apricot'
print(my_list)

my_dict = {'Apple':'Яблоко', 'Banana':'Банан', 'Peach':'Персик', 'Pear':'Груша', 'Pineapple':'Ананас', 'Orange':'Апельсин'}
print(my_dict)
print('Перевод', my_dict['Orange'])
my_dict['Orange'] = 'Оранжевый'
print(my_dict)