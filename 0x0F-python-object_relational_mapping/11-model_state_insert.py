#!/usr/bin/python3
"""
11-model_state_insert.py

Functions
    main()
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    adds the State object “Louisiana” to the
    database hbtn_0e_6_usa
    """
    # Get arguments from command line
    route, username, password, database = sys.argv
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    # Creates a shema
    Base.metadata.create_all(engine)
    # Creates a session Class
    Session = sessionmaker(bind=engine)
    # Create session object
    session = Session()

    # Create new record
    new_state = State(name="Louisiana")

    # Insert data to table sheme (memory)
    session.add(new_state)
    # Send data to DB
    session.commit()

    # Query
    records = session.query(State).filter(
        State.name == new_state.name).first()

    # Show data
    if records is None:
        print("Not found")
    else:
        print("{}".format(records.id))
    session.close()


if __name__ == "__main__":
    main()
