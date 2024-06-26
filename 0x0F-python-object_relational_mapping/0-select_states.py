#!/usr/bin/python3
"""A script that lists lists all states
from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    from sys import argv
    if len(argv) < 4:
        print("Error: requirement is 3 arguments")
        sys.exit()
    import MySQLdb
    # user_name = argv[1]
    # password = argv[2]
    # db_name = argv[3]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    # cur.close()

    for state in states:
        print(state)
    cur.close()
    conn.close()
    # cur.close()
