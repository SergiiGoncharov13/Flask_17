from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey


engine = create_engine('sqlite:///alchemy_test.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(30))
    arcticles = relationship('Arcticle', back_populates='author')


class Arcticle(Base):
    __tablename__ = 'arcticles' 
    id = Column(Integer(), primary_key=True)
    title = Column(String(100))
    content = Column(String(400))
    user_id = Column(Integer(), ForeignKey('users.id'))
    author = relationship('User', back_populates='arcticles')


Base.metadata.create_all(engine)
Base.metadata.bind = engine

