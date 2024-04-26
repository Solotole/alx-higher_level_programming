#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) < 4:
        print("Error: reuqirement is 3 arguments")
        sys.exit()
    import MySQLdb
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user_name,
            passwd=password,
            db=db_name,
            charset="utf8"
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    conn.close()
    # cur.close()

    for state in states:
        print(state)
