#!/usr/bin/python3
"""list all states"""
import MySQLdb as sql
from sys import argv


def main(user, password, data, state):
    """print states"""
    data = sql.connect(host='localhost', user=user
            , password=password, db=data, port=3306)
    a = data.cursor()
    a.execute("""SELECT id, name FROM states 
            WHERE name=%s
            ORDER BY id;""",
            (state,))
    x = a.fetchall()
    for i in x:
        print(i)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
