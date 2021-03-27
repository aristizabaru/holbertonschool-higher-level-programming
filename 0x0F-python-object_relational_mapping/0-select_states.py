#!/usr/bin/python3
"""
module 0-select_states

Functions
    main()
"""
import MySQLdb
import sys


def main():
    """
    Select all records from states table in hbtn_0e_0_usa database
    """
    # Get arguments from command line
    route, username, password, database = sys.argv
    # Connect to DB
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    # Create cursor to execute queries and use with to close connections
    with db.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        # Display data
        rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    main()
