def add_title(title):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(title.center(50, '='))
            result = func(*args, **kwargs)
            print('=' * 50)
            return result

        return wrapper

    return decorator


class View:
    @add_title('Ожидание пользовательского ввода')
    def wait_user_answer(self):
        print('Доступные действия:\n'
              '1. Добавить новую статью\n'
              '2. Отобразить все статьи\n'
              '3. Найти статьи\n'
              '4. Удалить статью\n'
              'Выход. Завершить программу')
        query = input('Введите номер действия: ')
        return query

    @add_title('Добавление новой статьи')
    def add_new_article(self):
        dict_article = {'Название': None,
                        'Автор': None,
                        'Количество знаков': None,
                        'Издание': None,
                        'Аннотация': None}

        for key in dict_article.keys():
            dict_article[key] = input(f'Введите {key.lower()} статьи: ').capitalize()
        return dict_article

    @add_title('Список статей')
    def print_articles(self, articles):
        if articles:
            [print(i + 1, article) for i, article in enumerate(articles)]
        else:
            'Статьи не обнаружены'

    @add_title('Поиск статьи')
    def find_articles(self):
        criteria = input('Введите список слов для поиска через пробел: ').split()
        return criteria

    @add_title('Название статьи')
    def get_article_name(self):
        name = input('Введите название для удаления')
        return name

    @add_title('Неизвестная ошибка')
    def __throw_an_error__(self, error):
        print('Произошла какая-то ошибка:', error)

    @add_title('Дополнительная информация')
    def get_deleted_context(self):
        number = int(input('Введите номер статьи для удаления: '))
        return number

    @add_title('Результат удаления')
    def return_deleted_result(self, result):
        print(result)
