#!/usr/bin/python3
"""Base declaration and inheritance
"""
from sqlalchemy import Column, Integer, String, relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City

Base = declarative_base()


class State(Base):
    """states subclass to Base class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade="all, delete-orphan", backref='state')
