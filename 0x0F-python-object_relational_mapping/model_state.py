#!/usr/bin/python3
"""
Python file that contains the class definition of a State
and an instance Base = declarative_base()
State class: inherits from Base Tips, links to the MySQL table states
Must use the module SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): class table name
        id (int): class State id
        name (str): class State name
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
