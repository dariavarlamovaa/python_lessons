import sqlite3
from time import time
import re
from flask import url_for


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def _get_objects(self, table):
        try:
            self.__cur.execute(f'SELECT * from {table}')
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Failed while reading data')
        return []

    def get_menu(self):
        return self._get_objects('menu')

    def get_posts(self):
        return self._get_objects('posts')

    def get_post(self, post_id):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE url == "{post_id}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except IOError:
            print('Failed while searching for the post')
        return None, None

    def add_post(self, title, text, url):
        try:
            self.__cur.execute(f'SELECT COUNT() as "count" FROM posts WHERE url == "{url}"')
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Post with this url is already exists')
                return False
            base = url_for('static', filename='images')
            text = re.sub(r'(?P<tag><img\s+[^>]*src=)(?P<quote>[\'"])(?P<url>.*)(?P=quote)>', r'\g<tag>' + base + r'/\g<url>>', text)
            tm = time()
            self.__cur.execute('INSERT INTO posts VALUES (NULL, ?, ?, ?, ?)', (title, text, url, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Error while adding the post in Database', e)
            return False
        return True
