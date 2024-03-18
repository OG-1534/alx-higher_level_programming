#!/usr/bin/python3
"""
File that contains the class definition of a City
City class: inherits from Base (imported from model_state),
links to the MySQL table cities.
Must use the module SQLAlchemy
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): class table name
        id (int): class id
        name (str): class city name
        state_id (int): state of the
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
