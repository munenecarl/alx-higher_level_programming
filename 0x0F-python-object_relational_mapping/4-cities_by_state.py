#!/usr/bin/python3
"""lists all cities from the database"""

import sys
import MySQLdb

def main():
    """lists all cities from the database"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()
    query_string = """SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id; """
    cur.execute(query_string)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
