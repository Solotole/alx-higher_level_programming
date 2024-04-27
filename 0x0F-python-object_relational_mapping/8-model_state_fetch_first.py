#!/usr/bin/python3
"""script filtering our first state only"""
if __name__ == '__main__':
    list_tuple = []
    String = ""
    from sys import argv
    if len(argv) < 4:
        print("Error: 3 arguments are required")
        sys.argv()
    from model_state import Base, State
    from sqlalchemy import (create_engine, orm)
    String = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(String.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = orm.sessionmaker(bind=engine)
    session = Session()
    list_tuple = session.query(State).order_by(State.id).first()
    if list_tuple is None:
        print("empty table")
    else:
        print(f"{list_tuple.id}: {list_tuple.name}")
    session.close()
