from csv import reader, writer


class Film:
    def __init__(self, title, genres, producers, year, length, studio, actors):
        self.title = title
        self.genres = genres
        self.producers = producers
        self.year = year
        self.length = length
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return ', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])


class Model:
    def __init__(self, filename):
        self.filename = filename
        self.database = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = reader(f)
                self.database = []
                self.genres = ['Crime', 'Drama', 'Action', 'Biography', 'History',
                               'Adventure', 'Romance', 'Sci-Fi',
                               'Thriller', 'War', 'Fantasy', 'Animation']
                for string in data:
                    self.database.append(self.__string_to_film__(string))
        except FileNotFoundError:
            print('Error in loading database. Proceed with empty data.')

    def __string_to_film__(self, string):
        title = string.pop(0)
        genres = []
        while string[0] in self.genres:
            genres.append(string.pop(0))
        producers = []
        while not string[0].isdigit():
            producers.append(string.pop(0))
        year = string.pop(0)
        length = string.pop(0)
        studio = string.pop(0)
        actors = {string[i]: string[i + 1] for i in range(0, len(string) - 1, 2)}
        return Film(title, genres, producers, year, length, studio, actors)

    @staticmethod
    def __film_to_string__(film):
        result = [film.title]
        result.extend(film.genres)
        result.extend(film.producers)
        result.extend([film.year, film.length, film.studio])
        [(result.append(key), result.append(value)) for key, value in film.actors.items()]
        return result

    def __save_data__(self):
        with open(self.filename, 'w', encoding='utf-8', newline='') as csv_file:
            data_writer = writer(csv_file)
            data_writer.writerows(map(self.__film_to_string__, self.database))

    def add_film(self, film_data):
        self.database.append(self.__string_to_film__(film_data))
        self.__save_data__()

    def get_films_by(self, words):
        words = list(map(str.strip, words.split(',')))
        films = []
        for word in words:
            for film in self.database:
                if word in ' '.join(map(str, film.__dict__.values())) and film not in films:
                    films.append(film)
        return films

    def remove_film(self, film):
        self.database.remove(film)
        self.__save_data__()
