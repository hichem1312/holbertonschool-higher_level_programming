#!/usr/bin/python3
"""Show states in database."""
import MySQLdb as sql
from sys import argv


def main(user, password, data):
    """Show cities in database and print result in order."""
    data = sql.connect(host='localhost', user=user
            , password=password, db=data, port=3306)
    a = data.cursor()
    a.execute("""
            SELECT c.id, c.name, s.name FROM cities c
            INNER JOIN states s ON s.id = c.state_id
            ORDER BY id;
            """)
    x = a.fetchall()
    for i in x:
        print(i)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
