#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    if len(argv) < 5:
        print("Error: script requiring 4 aruments")
        exit()
    import MySQLdb
    tuple_4 = (argv[4],)

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    cur.execute(("SELECT cities.name FROM states \
                JOIN cities ON cities.state_id = states.id \
                WHERE states.name = %s ORDER \
                BY cities.id ASC"), tuple_4)
    cities = cur.fetchall()
    for i in range(len(cities)):
        if i == len(cities) - 1:
            print(f"{cities[i][0]}")
        elif i != len(cities) - 1:
            print("{}".format(cities[i][0]), end=", ")
    cur.close()
    conn.close()
