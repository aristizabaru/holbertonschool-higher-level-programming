#!/usr/bin/python3
"""
module relationship_city

Classes
    City()
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Create Cities objects and maps them
    to cities table in DB

    Attributes
        id(int): Auto_increment integer
        name(string): name of state, max 128 chars
        state_id(int): Foreign key to states table primary key
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
