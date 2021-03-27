#!/usr/bin/python3
"""
12-model_state_update_id_2.py

Functions
    main()
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    changes the name of a State object
    from the database hbtn_0e_6_usa
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
    records = session.query(State).filter(
        State.id == 2).first()

    # Show data
    if records is None:
        print("Not found")
    else:
        records.name = "New Mexico"

    # Commit changes
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
