#!/usr/bin/python3
"""prints all states using sqlalchemy"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import City
from model_state import State

def main():
    """lists all State object from the database"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database, pool_pre_ping=True))
    sessions = sessionmaker(bind= engine)
    session = sessions()
    results = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

if __name__ == "__main__":
    main()
