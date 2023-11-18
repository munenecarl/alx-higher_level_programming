#!/usr/bin/python3
"""lists all cities of a specified state from the database"""

import sys
import MySQLdb

def main():
    """lists all cities of a specified state from the database"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()
    query_string = """SELECT cities.name
                      FROM cities
                      JOIN states ON cities.state_id = states.id
                      WHERE states.name = %s
                      ORDER BY cities.id ASC"""
    params = (state_name, )
    cur.execute(query_string, params)
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
