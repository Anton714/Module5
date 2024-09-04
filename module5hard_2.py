import time


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:

    def __init__(self, current_user: str = None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname: str, password: str):
        for i in self.users:
            if nickname == i.nickname and hash(password) == i.password:
                user = User(nickname, password)
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        for i in self.users:
            if i.nickname == nickname:
                print(f"\033[31mПользователь {nickname} уже существует\033[0m")
                return

        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, str_: str):
        list_vid = []
        for video in self.videos:
            if str_.lower() in video.title.lower():
                list_vid.append(video.title)
        return list_vid

    def watch_video(self, video: str):
        if self.current_user == None:
            print('\033[32mВойдите в аккаунт, чтобы смотреть видео\033[0m')
            return
        for j in self.videos:
            if j.title == video:
                if j.adult_mode and self.current_user.age < 18:
                    print('\033[31mВам нет 18 лет, пожалуйста, покиньте страницу\033[0m')
                    return
                print(f'\033[32mВоспроизводится: {video}\033[0m')
                for i in range(j.duration):
                    print('\033[34m', i, end=' ', )
                    j.time_now += 1
                    time.sleep(1)
                j.time_now = 0
                print('Конец видео\033[0m')
                time.sleep(1)


if __name__ == '__main__':
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
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
