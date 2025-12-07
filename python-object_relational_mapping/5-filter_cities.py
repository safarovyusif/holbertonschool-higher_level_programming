#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state.
Safe from SQL injection.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Bazaya qoşuluruq
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    # Sorğu: Ştatın adına görə şəhərləri tapırıq (JOIN istifadə edərək)
    # Təhlükəsizlik üçün %s istifadə edirik
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    # Formatlama: Tuple-lardan təmiz adları çıxarıb vergüllə birləşdiririk
    # row[0] - hər sətirdəki şəhər adıdır
    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()
