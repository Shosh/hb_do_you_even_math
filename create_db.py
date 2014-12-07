from connection import Base
from sqlalchemy import Column, Integer, String


class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    user = Column(String)
    score = Column(Integer)

    def __str__(self):
        return '{} with {} points'.format(self.user, self.score)

    def __repr__(self):
        return self.__str__()
    
