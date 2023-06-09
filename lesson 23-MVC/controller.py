from model import Model, DecodeError
from view import View


class Controller:
    def __init__(self):
        self.view = View()

        try:
            self.model = Model()
        except DecodeError as e:
            self.view.__throw_an_error__(e)

    def run(self):
        query = None
        while query != 'Выход':
            query = self.view.wait_user_answer()
            self.check_user_answer(query)

    def check_user_answer(self, query):
        if query == '1':
            article_data = self.view.add_new_article()
            self.model.add_new_article(article_data)
        elif query == '2':
            all_articles = self.model.articles
            self.view.print_articles(all_articles)
        elif query == '3':
            criteria = self.view.find_articles()
            article = self.model.find_articles(criteria)
            self.view.print_articles(article)
        elif query == '4':
            article_name = self.view.get_article_name()
            articles = self.model.find_articles([article_name])
            result = self.model.delete_article(articles)
            if result == 'Слишком много статей':
                self.view.print_articles(articles)
                number = self.view.get_deleted_context()
                result = self.model.delete_article((articles[number - 1]))
            self.view.return_deleted_result(result)
