#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
where name matches the argument (safe from MySQL injection).
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # TƏHLÜKƏSİZ YOL: %s istifadə edirik və arqumenti tuple kimi ötürürük
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
