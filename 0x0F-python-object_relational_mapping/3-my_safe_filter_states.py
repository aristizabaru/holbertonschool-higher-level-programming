#!/usr/bin/python3
"""
module 3-my_safe_filter_states

Functions
    main()
"""
import MySQLdb
import sys


def main():
    """
    Select all records from states table in hbtn_0e_0_usa database
    where the name value = lookup variable while protecting
    from SQL injection
    """
    # Get arguments from command line
    route, username, password, database, lookup = sys.argv
    # Compose query
    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    # Connect to DB
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    # Create cursor to execute queries and use with to close connections
    with db.cursor() as cur:
        cur.execute(query, (lookup,))
        # Display data
        rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()


if __name__ == "__main__":
    main()
