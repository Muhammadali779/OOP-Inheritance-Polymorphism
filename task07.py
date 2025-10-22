class Media:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def play(self):
        print(f"Playing media: {self.title} ({self.duration} min)")


class Song(Media):
    def __init__(self, title, duration, artist):
        self.title = title
        self.duration = duration
        self.artist = artist

    def play(self):
        print(f"♻️  Ovoz berilmoqda: '{self.title}' — {self.artist} ({self.duration} daqiqa)")


class Movie(Media):
    def __init__(self, title, duration, director):
        self.title = title
        self.duration = duration
        self.director = director

    def play(self):
        print(f"♻️  Film namoyishi: '{self.title}', rejissyor: {self.director} ({self.duration} daqiqa)")


class Podcast(Media):
    def __init__(self, title, duration, host):
        self.title = title
        self.duration = duration
        self.host = host

    def play(self):
        print(f"♻️  Podkast eshittirilmoqda: '{self.title}' — boshlovchi: {self.host} ({self.duration} daqiqa)")


media_list = [
    Song("Qizil Atirgul", 4, "Yagzon"),
    Movie("Erkinlik", 120, "Alisher Uzoqov"),
    Podcast("TexnoTalks", 45, "Eshmatjon Toshmatjonov")
]

for m in media_list:
    m.play()
