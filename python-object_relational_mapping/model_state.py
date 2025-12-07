#!/usr/bin/python3
"""
Definition of the State class and instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base obyektini yaradırıq (bu, bütün modellərin "anası" olacaq)
Base = declarative_base()


class State(Base):
    """
    State class:
    - inherits from Base
    - links to the MySQL table states
    """
    __tablename__ = 'states'  # Cədvəlin adı

    # id sütunu: unikal, boş ola bilməz, primary key, avtomatik artan
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # name sütunu: string (max 128), boş ola bilməz
    name = Column(String(128), nullable=False)
