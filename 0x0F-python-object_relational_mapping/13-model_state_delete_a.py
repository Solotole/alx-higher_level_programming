#!/usr/bin/python3
"""script that deletes a state from the table
   if State.name contain character 'a' or 'A'
"""

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
    list_tuple = session.query(State).filter(State.name.ilike('%a%')).all()
    for tuple_s in list_tuple:
        if 'a' in tuple_s.name or 'A' in tuple_s.name:
            session.delete(tuple_s)
    session.commit()
