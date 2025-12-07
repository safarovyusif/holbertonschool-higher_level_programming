#!/usr/bin/python3
"""
Contains the class definition of a City.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that inherits from Base and links to the MySQL table cities.
    """
    __tablename__ = 'cities'

    # Unikal ID, Primary Key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Şəhərin adı
    name = Column(String(128), nullable=False)

    # Ştatın ID-si (Foreign Key -> states.id)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
