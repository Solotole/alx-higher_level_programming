#!/usr/bin/python3
"""script filtering out all states"""
if __name__ == '__main__':
    list_tuple = []
    String = ""
    from sys import argv
    if len(argv) < 4:
        print("Error: script requires 3 aruments")
        sys.exit()
    from model_state import Base, State
    from sqlalchemy import (create_engine, orm)
    String = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(String.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = orm.sessionmaker(bind=engine)
    session = Session()
    list_tuples = session.query(State.id, State.name).order_by(State.id).all()
    for state_id, state_name in (list_tuples):
        print(f"{state_id}: {state_name}")
