#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py

Functions
    main()
"""
import sys
from model_state import Base, State
from model_city import City
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
    records = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)

    # print results
    for state_record, city_record in records:
        print("{}: ({}) {}".format(
            state_record.name, city_record.id, city_record.name))

    session.close()


if __name__ == "__main__":
    main()
