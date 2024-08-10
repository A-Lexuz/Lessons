from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, knight_name, power):
        self.knight_name = knight_name
        self.power = power
        super().__init__()

    def run(self):
        current_enemy = 100
        today = 0
        print(f'{self.knight_name}, we under attack! Enemy has {current_enemy} warriors\n')

        while current_enemy > 0:
            sleep(1)
            current_enemy -= self.power
            today += 1
            print(f'{self.knight_name} fights for {today} days, {current_enemy} warriors left\n')

        print(f'{self.knight_name } won for {today} days!\n')

knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight('Sir Galahad', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("The battles are over... this time")