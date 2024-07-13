import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    suscription_date =  Column(String(250), nullable=False)
    favorites = relationship('favorite')


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    manofacturer = Column(String(50), nullable=False)
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)

    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    favorite_id = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    persons = relationship('person')
    vehicles = relationship('vehicle')
    planets = relationship('planet')
    persons = relationship('person')



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')