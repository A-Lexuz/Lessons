def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(6, False)
print_params()
print_params(6, 'число', None)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, True, "строка"]
values_dict = {'a': "str", 'b': 6, 'c': False }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [32, 'Зубы']
print_params(*values_list_2, 42)