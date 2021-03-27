#!/usr/bin/python3
"""
module model_state

Classes
    State()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Create State objects and maps them
    to states table in DB

    Attributes
        id(int): Auto_increment integer
        name(string): name of state, max 128 chars
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
