#!/usr/bin/python3
"""
101-relationship_states_cities_list.py

Functions
    main()
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
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
    records = session.query(State).order_by(State.id)

    # print results
    for record in records:
        print("{}: {}".format(record.id, record.name))
        for relationship in record.cities:
            print("\t{}: {}".format(
                relationship.id, relationship.name))

    session.close()


if __name__ == "__main__":
    main()
