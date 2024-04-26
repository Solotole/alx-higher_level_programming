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
    host = "localhost"
    port = 3306

    conn = MySQLdb.connect(host, port, user_name, password, db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    conn.clode()
    # cur.close()

    for state in states:
        print(state)
