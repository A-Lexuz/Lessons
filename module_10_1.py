from time import sleep
from datetime import datetime
from threading import Thread
def wite_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(f'Какое-то слово №{i}\n')
            sleep(0.1)
            file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start1 = datetime.now()

wite_words(10,'example1.txt')
wite_words(30,'example2.txt')
wite_words(200,'example3.txt')
wite_words(100,'example4.txt')

time_end1 = datetime.now()

print(f"Работа функции в одном потоке заняла: {time_end1 - time_start1} секунд")

time_start2 = datetime.now()

first_thread = Thread(target=wite_words, args = (10,'example5.txt'))
second_thread = Thread(target=wite_words, args = (30,'example6.txt'))
third_thread = Thread(target=wite_words, args = (200,'example7.txt'))
fourth_thread = Thread(target=wite_words, args = (100,'example8.txt'))

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()

time_end2 = datetime.now()

print(f"Работа функции в четырёх потоках заняла: {time_end2 - time_start2} секунд")