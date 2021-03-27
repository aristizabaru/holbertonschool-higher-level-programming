#!/usr/bin/python3
"""
module relationship_state

Classes
    State()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

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
    # The new way to go in order to build relationships
    # is relationship.back_populates
    cities = relationship("City", backref="state")
