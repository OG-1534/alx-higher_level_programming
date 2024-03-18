#!/usr/bin/python3
"""
Script that defines a State class and a Base class
Works with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ (str): class table name
        id (int): class State id
        name (str): class State name
        cities (:obj:`City`): Cities of the State
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
