#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Takes 3 arguments: username, password, database name.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Bazaya qoşulma
    # sys.argv[1] = username, sys.argv[2] = password, sys.argv[3] = db_name
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Kursor yaradılır
    cur = db.cursor()

    # SQL sorğusu icra edilir (id-yə görə artan sıra ilə)
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Bütün nəticələr götürülür
    rows = cur.fetchall()

    # Nəticələr çap edilir
    for row in rows:
        print(row)

    # Kursor və baza bağlanır
    cur.close()
    db.close()
