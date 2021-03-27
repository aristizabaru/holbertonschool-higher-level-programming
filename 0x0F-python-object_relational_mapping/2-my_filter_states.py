#!/usr/bin/python3
"""
module 2-my_filter_states

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
    # Connect to DB
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    # Create cursor to execute queries and use with to close connections
    with db.cursor() as cur:
        cur.execute("""
        SELECT * FROM states
        WHERE name = '{}'
        ORDER BY states.id ASC
        """.format(lookup))
        # Display data
        rows = cur.fetchall()
    for row in rows:
        if row[1] == lookup:
            print(row)
    db.close()


if __name__ == "__main__":
    main()
