#!/usr/bin/python3
"""list all states"""
import MySQLdb as sql
from sys import argv


def main(user, password, db):
    """print states"""
    db = sql.connect(host='localhost', user=user, password=password, db=db, port=3306)
    c = db.cursor()
    c.execute("""SELECT id, name FROM states ORDER BY id;""")
    x = c.fetchall()
    for i in x:
        print(i)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
