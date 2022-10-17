#!/usr/bin/python3
"""list all states"""
import MySQLdb as sql
from sys import argv


def main(user, password, data, state):
    """print states"""
    data = sql.connect(host='localhost', user=user,
                       password=password, db=data, port=3306)
    a = data.cursor()
    a.execute("""SELECT c.name FROM cities c
            INNER JOIN states s ON s.id = c.state_id
            WHERE s.name = %s
            ORDER BY c.id;""", (state,))
    x = a.fetchall()
    le = []
    for i in x:
        le.append(i[0])
    print(', '.join(le))


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
