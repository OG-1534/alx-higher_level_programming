#!/usr/bin/python3
"""
Script that defines a City class, an improvement of model_city.py
Work swith MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ (str): Class table name
        id (int): class id
        name (str): class name
        state_id (int): City of the state
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
