from sqlalchemy import Integer, String, Column
from models.database import Base
from sqlalchemy.orm import relationship


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(100), nullable=False)
    student = relationship('Student')

    def __repr__(self):
        return f'Группа(Id: {self.id}, Name: {self.group_name})'