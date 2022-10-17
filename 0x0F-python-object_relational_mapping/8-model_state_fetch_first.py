#!/usr/bin/python3
"""List states with orm"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    data = argv[3]

    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                        (user, password, data), pool_pre_ping=True)
    Base.metadata.create_all(eng)

    session = Session(eng)
    state = session.query(State).first()

    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
