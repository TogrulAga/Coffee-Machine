class Movie:
    # create class here
    def __init__(self, title: str, director: str, year: int):
        self.title = title
        self.director = director
        self.year = year


# objects of the class Movie
titanic = Movie(title="Titanic", director="James Cameron", year=1997)
star_wars = Movie(title="Star Wars", director="George Lucas", year=1977)
fight_club = Movie(title="Fight Club", director="David Fincher", year=1999)
