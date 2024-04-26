#!/usr/bin/python3
"""script that takes in an argument and displays all
   values in the states table of hbtn_0e_0_usa
   where name matches the argument.
"""

if __name__ == "__main__":
    from sys import argv
    execution_string = ""
    if len(argv) < 5:
        print("Error: code requires 4 aruments to run")
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
    execution_string = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cur.execute(execution_string.format(argv[4]))
    states = cur.fetchall()

    for state in states:
        if state[1] == argv[4]:
            print(state)
    cur.close()
    conn.close()
