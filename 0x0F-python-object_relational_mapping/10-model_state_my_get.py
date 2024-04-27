#!/usr/bin/python3
"""script filtering out all states"""
if __name__ == '__main__':
    count_id = 0
    String = ""
    from sys import argv, exit
    if len(argv) < 5:
        print("Error: script requires 4 arguments")
        exit()
    tuple_4 = argv[4]
    from model_state import Base, State
    from sqlalchemy import (create_engine, orm)
    String = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(String.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = orm.sessionmaker(bind=engine)
    session = Session()
    count_id = session.query(State.id).filter(State.name.like(tuple_4)) \
        .order_by(State.id).all()
    for tuple_s in count_id:
        if len(tuple_s) == 0:
            print("Not found")
        elif len(tuple_s) != 0:
            print(f'{tuple_s[0]}')
    session.close()
