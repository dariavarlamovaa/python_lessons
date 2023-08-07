from faker import Faker

from models.database import create_db, Session
from models.groups import Group
from models.lessons import Lesson
from models.students import Student


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    lessons = ['Математика', 'Физика', 'Информатика', 'Философия',
               'Линейная алгебра', 'Математический анализ', 'Физкультура']

    group1 = Group(group_name='Z010')
    group2 = Group(group_name='V020')

    session.add(group1)
    session.add(group2)
    for key, les in enumerate(lessons):
        lesson = Lesson(lesson_title=les)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.append(group2)
        session.add(lesson)

    session.commit()

    faker = Faker('ru_Ru')
    groups = [group1, group2]

    for _ in range(50):
        fullname = faker.name().split()
        age = faker.random.randint(18, 25)
        group = faker.random.choice(groups)
        student = Student(fullname, age, group.id)
        session.add(student)

    session.commit()
    session.close()