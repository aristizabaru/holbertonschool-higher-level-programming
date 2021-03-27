#!/usr/bin/python3
"""
13-model_state_delete_a.py

Functions
    main()
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    deletes all State objects with a name
    containing the letter a from the database hbtn_0e_6_usa
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

    # Query
    session.query(State).filter(
        State.name.like('%a%')).delete(synchronize_session=False)

    # Commit changes
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
