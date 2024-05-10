
def print_params(miss):
    rate = 10 - miss
    if rate == 1:
        print ('Оценка за выполненную работу -', rate, 'балл')
    if 2 <= rate < 5:
        print('Оценка за выполненную работу -', rate, 'балла')
    if 5 <= rate <= 10 or rate == 0:
        print ('Оценка за выполненную работу -', rate, 'баллов')

#В данном блоке прописываем количество ошибок
print_params(10)
print_params(6)
print_params(3)