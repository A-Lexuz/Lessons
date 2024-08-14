from threading import Thread
from random import randint
from time import sleep
import queue

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self,guest_name):
        self.guest_name = guest_name
        super().__init__()

    def run(self):
        sleep(randint(2,8))


class Cafe:
    def __init__(self,tables):
        self.queue = queue.Queue() #очередь гостей
        self.tables = tables #список столов


    def guest_arrival(self,*guests):
        for guest in guests:
            print(f'{guest.guest_name} прибыл')
            guest_eating = 0
            for table in tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.guest_name} сел за {table.number} стол')
                    guest_eating = 1
                    break
            if guest_eating == 0:
                print(f'{guest.guest_name} ушел в очередь')
                self.queue.put(guest)

    def discuss_guests(self):
         while not self.queue.empty() or any(x.guest for x in tables):
             for table in tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'Гость {table.guest.guest_name} покушал и ушёл, стол №{table.number} освободился')
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f'Гость {table.guest.guest_name} вышел из очереди и сел за стол №{table.number}')












tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_names]

cafe = Cafe(tables)

cafe.guest_arrival(*guests)
cafe.discuss_guests()
