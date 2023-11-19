#!/usr/bin/python3
"""prints the State object with the name passed as argument"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import State

def main():
    """lists the State object with the name passed as argument"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")

if __name__ == "__main__":
    main()
