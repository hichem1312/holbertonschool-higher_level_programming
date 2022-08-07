#!/usr/bin/python3
"""state table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class state(base):
    """state class."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True
            , autoincrement=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
