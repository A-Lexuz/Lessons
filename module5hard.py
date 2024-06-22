
from time import sleep

class UrTube:
    def __init__(self):
        self.users = {}
        self.users_data = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users[nickname] = hash(password)
            self.current_user = User(nickname, password, age)
            user = User(nickname, password, age)
            self.users_data.append(user)

    def log_in(self, login, password):
        if login not in self.users:
            print(f'Пользователя {login} не существует, пожалуйста зарегистрируйтесь.')
        elif login in self.users and hash(password) == self.users[login]:
            for i in self.users_data:
                if login == i.nickname:
                    self.current_user = i
        else:
            print("Неверный пароль, попробуйте еще раз")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, key):
        search_result = []
        for video in self.videos:
            if key.lower() in video.title.lower():
                search_result.append(video.title)
        return search_result

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for i in self.videos:
                if title == i.title:
                    if i.adult_mode == True and self.current_user.age < 18:
                        print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    else:
                        while i.time_now < i.duration:
                            print(i.time_now, end='')
                            sleep(0.25)
                            print('.', end='')
                            sleep(0.25)
                            print('.', end='')
                            sleep(0.25)
                            print('.', end='')
                            sleep(0.25)
                            i.time_now += 1
                        if i.time_now == i.duration:
                            print(i.time_now, end="...")
                            print('Конец видео')

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
