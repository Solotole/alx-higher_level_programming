#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    if len(argv) < 3:
        print("Error: scripts uses 3 arguments")
        sys.ext()
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
    cur.execute("SELECT cities.id, cities.name, states.name FROM states JOIN \
            cities ON cities.state_id = states.id ORDER BY cities.id ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    conn.close()
