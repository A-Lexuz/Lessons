from threading import Thread, Lock
from time import sleep
from random import randint

class Bank():

    def __init__(self,balance):
        self.balance = balance
        self.lock = Lock()


    def deposit(self):
        for i in range(100):
            a = randint(50, 500)

            self.balance += a
            print(f'Пополнение баланса на {a}, Текущий баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked() is True:
                self.lock.release()
            sleep(0.1)

    def take(self):

        for i in range(100):
            a = randint(50,500)
            print(f'Запрос на {a}')
            if self.balance >= a:
                self.balance -= a
                print(f'Снятие {a} средств произошло успешно. Баланс {self.balance}')
            else:
                print(f'Запрос на снятие {a} средств отклонён. Недостаточно средств')
                self.lock.acquire()
            sleep(0.1)

bk = Bank(200)

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')