#!/usr/bin/python3
"""script that adds a state into the table"""

if __name__ == '__main__':
    tuple_instance = []
    list_tuple = []
    from sys import argv
    if len(argv) < 4:
        print("Error: 3 arguments are required")
        sys.exit()
    from model_state import Base, State
    from sqlalchemy import (create_engine, orm)
    String = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(String.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = orm.sessionmaker(bind=engine)
    session = Session()
    tuple_instance = State(name='Louisiana')
    session.add(tuple_instance)
    session.commit()
    list_tuple = session.query(State.id, State.name).filter(State.name == 'Louisiana').all()
    for listing in list_tuple:
        if len(listing) != 0 and listing[1] == 'Louisiana':
            print(f"{listing[0]}")
        elif len(listsing) == 0:
            print("new state not added")
