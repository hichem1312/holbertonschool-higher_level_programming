#!/usr/bin/python3
"""List first state using ORM."""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main(user, password, data):
    """List first state in database and print result in order."""
    engin = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, password, data), pool_pre_ping=True)
    Base.metadata.create_all(engin)
    Session = sessionmaker(bind=engin)
    s = Session()
    state = s.query(State).first()
    if state:
        print("{:d}: {:s}".format(state.id, state.name))
    else:
        print("Nothing")


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
