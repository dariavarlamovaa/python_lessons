from sqlalchemy import Integer, String, Column, ForeignKey
from models.database import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    patronymic = Column(String(100), nullable=False)
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, fullname, age, group):
        self.surname = fullname[0]
        self.name = fullname[1]
        self.patronymic = fullname[2]
        self.age = age
        self.group = group

    def __repr__(self):
        return f'Студент(ФИО: {self.surname} {self.name} {self.patronymic},' \
               f'Возраст: {self.age}, ' \
               f'Id группы: {self.group})'