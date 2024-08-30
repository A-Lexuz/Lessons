import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                if participant.speed * 2 >= self.full_distance:
                    while participant.speed * 2 >= self.full_distance:
                        self.full_distance *= 2
                    print(f'Наши бегуны слишком быстрые чтобы запечатлить результат, '
                          f'дистанция увеличена до {self.full_distance} метров')

                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[f'{place} место'] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)

        self.runner_2 = Runner('Андрей', 9)

        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(key, '\n')
            for u,y in value.items():
                print (u, y, '\n')


    def test_1(self):
        unreal_tournament = Tournament(90, self.runner_1, self.runner_3)
        all_results = unreal_tournament.start()
        result = list(all_results.values())
        self.assertTrue(result[-1] == 'Ник')
        self.all_results[f"Результат теста 1:"] = all_results

    def test_2(self):
        unreal_tournament = Tournament(50,  self.runner_2, self.runner_3)
        all_results = unreal_tournament.start()
        result = list(all_results.values())
        self.assertTrue(result[-1] == 'Ник')
        self.all_results[f"Результат теста 2:"] = all_results

    def test_3(self):
        unreal_tournament = Tournament(1,  self.runner_1, self.runner_2, self.runner_3)
        all_results = unreal_tournament.start()
        result = list(all_results.values())
        self.assertTrue(result[-1] == 'Ник')
        self.all_results[f"Результат теста 3:"] = all_results