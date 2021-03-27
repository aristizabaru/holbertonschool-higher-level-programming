#!/usr/bin/python3
"""
module 5-filter_cities

Functions
    main()
"""
import MySQLdb
import sys


def main():
    """
    Select all records from states table in hbtn_0e_0_usa database
    where the name value = lookup variable
    """
    # Get arguments from command line
    route, username, password, database, lookup = sys.argv
    # Compose query
    query = """
        SELECT cities.name FROM cities
        LEFT JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    # Connect to DB
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    # Create cursor to execute queries and use with to close connections
    with db.cursor() as cur:
        cur.execute(query, (lookup,))
        # Display data
        rows = cur.fetchall()
    print(', '.join([str(row[0]) for row in rows]))
    db.close()


if __name__ == "__main__":
    main()
