#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=user_name, passwd=password, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)
    cur.close()
    conn.close()
