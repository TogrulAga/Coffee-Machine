class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    @property
    def info(self):
        return f'\"{self.title}\" by {self.artist} ({self.year}) hangs in the {Painting.museum}.'


painting = Painting(title=input(), artist=input(), year=int(input()))
print(painting.info)
