# import sqlite3 as sq


# def read_avatar(filename):
#     try:
#         with open(f'avatars/{filename}', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return None
#
#
# def write_avatar(filepath, data):
#     try:
#         with open(filepath, 'wb') as f:
#             f.write(data)
#             return True
#     except IOError as e:
#         print(e)
#         return False


# with sq.connect('cars.db') as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute('''SELECT * FROM cars''')
#     for car in cur:
#         print(car['model'])
#
#     cur.execute('''CREATE TABLE IF NOT EXISTS users(
#                     user_id INTEGER PRIMARY KEY,
#                     avatar BLOB,
#                     name TEXT
#                 )''')
#
#     img = read_avatar('1.png')
#     sqlite_img = sq.Binary(img)
#     cur.execute('''INSERT INTO users VALUES (1, ?, ?)''', (sqlite_img, 'Василий'))
#
#     cur.execute('''SELECT avatar FROM users''')
#     img = cur.fetchone()[0]
#     write_avatar('avatars/2.png', img)
#
#     creating backup file ----------------------
#
#     with open('cars_backup.sql', 'w') as f:
#         for i in con.iterdump():
#             f.write(f'{i}\n')
#
#     sql_script = open('cars_backup.sql').read()
#     cur.executescript(sql_script)

# with sq.connect(':memory:') as con:
#     cur = con.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS users(
#                     user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     avatar BLOB,
#                     name TEXT
#                 )''')
#
#     cur.executemany('''INSERT INTO users VALUES (NULL, ?, ?)''', [(i, i**2) for i in range(10)])
#     cur.execute('SELECT * FROM users')
#     print(cur.fetchall())


# ---------------------STUDENTS ---------------------
# import os
#
# from sqlalchemy import or_, not_, desc, func, text
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator

# from models.groups import Group
# from models.lessons import Lesson, association_table
# from models.students import Student

# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
#     ---------------------МЕТОДЫ СЕССИИ---------------------
#     ---------------------Получить все объекты---------------------
#     print(session.query(Lesson).all())
#
#     for lesson in session.query(Lesson).all():
#         print(lesson.lesson_title, lesson.groups)
#
#     for group in session.query(Group).all():
#         print(group.group_name, group.lessons)
#
#     print(session.get(Lesson, 3))
#
#     for lesson in session.query(Lesson).filter(Lesson.id < 3, Lesson.lesson_title.startswith('Ф')):
#         print(lesson)
#
#     ---------------------Связь---------------------
#     for lesson, gr in session.query(Lesson.lesson_title, Group.group_name).filter(
#         association_table.c.lesson_id == Lesson.id,
#         association_table.c.group_id == Group.id
#     ):
#         print(lesson, gr)
#
#     --------------------IN/NOT IN--------------------
#     print(session.query(Lesson).filter(Lesson.id.in_([1, 2, 3])).all())
#     print(session.query(Lesson).filter(Lesson.id.notin_([1, 2, 3])).all())
#
#     --------------------BETWEEN/NOT BETWEEN--------------------
#     print(session.query(Student).filter(Student.age.between(18, 20)).all())
#     print(session.query(Student).filter(not_(Student.age.between(18, 20)).all()))
#
#     --------------------LIKE, LIMIT, OFFSET--------------------
#     print(session.query(Student).filter(Student.age.like('2%')).all())
#     print(session.query(Student).filter(Student.age.like('1_')).limit(4).offset(2).all())
#
#     --------------------ORDER BY(DESC)--------------------
#     for student in session.query(Student).filter(Student.age.like('1%')).order_by(Student.surname).all():
#         print(student)
#     for student in session.query(Student).filter(Student.age.like('1%')).order_by(desc(Student.surname)).all():
#         print(student)
#
#     --------------------JOIN--------------------
#     for it in session.query(Student, Group).join(Group).filter(Group.group_name == 'Z010'):
#         print(it)
#
#     --------------------JOIN + HAVING--------------------
#     for it in session.query(Group.group_name, func.count(Student.id)).join(Group).group_by(Group.id)\
#             .having(func.count(Student.id) > 25):
#         print(it)
#
#     --------------------TEXT--------------------
#     for it in session.query(Student).filter(text('surname LIKE "М%"')):
#         print(it)