from project.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    name = Column(String)

    def __str__(self):
        return f'User(id={self.id})'

    def __repr__(self):
        return str(self)
