#!/usr/bin/python3
"""
module 4-cities_by_state

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
    route, username, password, database = sys.argv
    # Compose query
    query = "SELECT * FROM cities ORDER BY cities.id ASC LIMIT 15"
    # Connect to DB
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    # Create cursor to execute queries and use with to close connections
    with db.cursor() as cur:
        cur.execute(query)
        # Display data
        rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    main()
