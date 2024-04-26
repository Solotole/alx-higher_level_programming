#!/usr/bin/python3
"""script that lists all states with
a name starting with N from the database
hbtn_0e_0_usa
"""

if __name__ == "__main__":
    from sys import argv

    if len(argv) < 4:
        print("Error: used arguments should be 3")
        sys.exit()
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)
    cur.close()
    conn.close()
