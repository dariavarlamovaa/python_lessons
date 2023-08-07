from sqlalchemy import Integer, String, Column, ForeignKey, Table
from models.database import Base
from sqlalchemy.orm import relationship

association_table = Table('association', Base.metadata,
                          Column('group_id', Integer, ForeignKey('groups.id')),
                          Column('lesson_id', Integer, ForeignKey('lessons.id')))


class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lesson_title = Column(String(100), nullable=False)
    groups = relationship('Group', secondary='association', backref='lessons')

    def __repr__(self):
        return f'Дисциплина:(Id: {self.id}, ' \
               f'Название: {self.lesson_title})'