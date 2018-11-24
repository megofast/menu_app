import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    name = Column(String(80), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
            'name' : self.name,
            'email' : self.email,
            'picture' : self.picture,
            'id' : self.id,
        }

class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
        'name' : self.name,
        'id' : self.id,
        'user' : self.user_id,
        }

class MenuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'name' : self.name,
            'description' : self.description,
            'id' : self.id,
            'price' : self.price,
            'course' : self.course,
            'user' : self.user_id,
        }

################ EOF ########################
engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.create_all(engine)
