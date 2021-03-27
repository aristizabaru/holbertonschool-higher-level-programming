#!/usr/bin/python3
"""
100-relationship_states_cities.py

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
    creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
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

    # Create new records
    new_state = State(name="California")
    new_city = City(name="San Francisco")

    # Insert new_city into new_state collection
    new_state.cities.append(new_city)

    # Insert data to table sheme (memory)
    session.add(new_state)

    # Send data to DB
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
