print ("Добро пожаловать в генератор паролей для 'Слишком древнего шифра'")
n = int(input('Введите число камней в первом поле (3-20): '))
row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
row1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []
for i in row:
    for u in row1:
        if n % (i + u) == 0 and u > i:
            result.append(i)
            result.append(u)
result1 = ''
for p in result:
    result1 += str(p)

print('Шифр:', result1)