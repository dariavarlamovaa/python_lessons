import json


class Article:
    def __init__(self, title, author, symbols, publisher, annotation):
        self.title = title
        self.autor = author
        self.symbols = symbols
        self.publisher = publisher
        self.annotation = annotation

    def __str__(self):
        return f'{self.title} - {self.autor}'


class DecodeError(Exception):
    pass


class Model:
    def __init__(self):
        self.filepath = 'db.txt'
        self.__articles = {}
        try:
            self.data = json.load(open(self.filepath, 'r'))
            for article in self.data.values():
                self.__articles[f'{article["title"]} {article["author"]}'] = Article(*article.values())
        except json.JSONDecodeError:
            raise DecodeError

        except FileNotFoundError:
            with open(self.filepath, 'w') as f:
                f.write('{}')  # чтобы json смог работать с файлом

    @property
    def articles(self):
        return self.__articles

    def add_new_article(self, article_data):
        new_article = Article(*article_data.values())
        self.__articles[f'{new_article.title} {new_article.autor}'] = new_article
        dict_articles = {art.title: art.__dict__ for art in self.__articles.values()}
        json.dump(dict_articles, open(self.filepath, 'w'))

    def find_articles(self, criteria):
        articles = []
        for article in self.__articles.values():
            for crit in criteria:
                if article in articles:
                    break
                for attr in article.__dict__.values():
                    if crit.lower() in attr.lower():
                        articles.append(article)
                        break
        return articles

    def delete_article(self, articles):
        if len(articles) == 0:
            return 'Такая статья не была найдена'
        elif len(articles) == 1:
            article = articles[0]
            key = f'{article.title} {article.autor}'
            self.__articles.pop(key)
            return 'Стать была удалена'
        else:
            return 'Слишком много статей'

