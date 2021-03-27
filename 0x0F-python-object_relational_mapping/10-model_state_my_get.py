#!/usr/bin/python3
"""
10-model_state_my_get.py

Functions
    main()
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa
    """
    # Get arguments from command line
    route, username, password, database, lookup = sys.argv
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    # Creates a shema
    Base.metadata.create_all(engine)
    # Creates a session Class
    Session = sessionmaker(bind=engine)
    # Create session object
    session = Session()

    # Query
    records = session.query(State).filter(
        State.name == lookup).first()

    # Show data
    if records is None:
        print("Not found")
    else:
        print("{}".format(records.id))

    session.close()


if __name__ == "__main__":
    main()
