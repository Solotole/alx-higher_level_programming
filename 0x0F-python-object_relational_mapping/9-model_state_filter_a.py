#!/usr/bin/python3
"""script filtering out all states with character a or A"""
if __name__ == '__main__':
    list_tuple = []
    String = ""
    from sys import argv
    if len(argv) < 4:
        print("Error: 3 aruments are required")
        sys.exit()
    from model_state import Base, State
    from sqlalchemy import (create_engine, orm)
    String = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(String.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = orm.sessionmaker(bind=engine)
    session = Session()
    list_tuples = session.query(State.id, State.name)\
            .filter(State.name.ilike('%a%')).order_by(State.id).all()
    for tuple_s in list_tuples:
        if 'a' in tuple_s[1] or 'A' in tuple_s[1]:
            print(f"{tuple_s[0]}: {tuple_s[1]}")
