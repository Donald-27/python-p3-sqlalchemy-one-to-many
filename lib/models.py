from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

# Set up the engine and base
engine = create_engine('sqlite:///one_to_many.db')
Base = declarative_base()

# Game model (one game has many reviews)
class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    # One-to-many relationship
    reviews = relationship('Review', backref=backref('game'))

    def __repr__(self):
        return f'Game(id={self.id}, title="{self.title}", platform="{self.platform}")'

# Review model (each review belongs to one game)
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    comment = Column(String())
    game_id = Column(Integer(), ForeignKey('games.id'))

    def __repr__(self):
        return f'Review(id={self.id}, score={self.score}, game_id={self.game_id})'
