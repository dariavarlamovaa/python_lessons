class View:
    def wait_user_answer(self):
        print('Awaiting your answer')
        print('1. Add a new film\n'
              '2. Get films by ...\n'
              '3. Remove film\n'
              'Quit. Exit the program')
        result = input('Your answer: ')
        return result

    def get_film_data(self):
        props = ['title', 'genre(comma separated)', 'producer', 'year',
                 'length', 'studio', 'actors(Actor: Role,...']
        raw_data = [input(f'Input {prop}: ') for prop in props]
        genres = list(map(str.strip, raw_data[1].split(',')))
        actors = [row.strip().split(':') for row in raw_data[-1].split(',')]
        data = raw_data[:1] + genres + raw_data[2:-1]
        [data.extend(row) for row in actors]
        return data

    def get_target(self):
        words = input('enter keywords to find films, comma separated: ')
        return words

    def print_films(self, films):
        [print(f'{i}. {film}') for i, film in enumerate(films, 1)]

    def get_deletion_contex(self, films):
        self.print_films(films)
        number = int(input('enter number of the film you want to delete:'))
        return number
