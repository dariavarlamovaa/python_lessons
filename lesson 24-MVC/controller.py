from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model('films.csv')

    def run(self):
        query = None
        while query != 'quit':
            query = self.view.wait_user_answer()
            self.eval_user_answer(query)

    def eval_user_answer(self, query):
        if query == '1':
            film_data = self.view.get_film_data()
            self.model.add_film(film_data)
        elif query == '2':
            target = self.view.get_target()
            films = self.model.get_films_by(target)
            self.view.print_films(films)
        elif query == '3':
            target = self.view.get_target()
            films = self.model.get_films_by(target)
            if len(films) > 1:
                number = self.view.get_deletion_contex(films)
                films = films[[number - 1]]
            self.model.remove_film(films[0])
