#!/usr/bin/python3
"""script that introduces relationship
"""

if __name__ == '__main__':
    list_tuple = []
    list_tuple1 = []
    from sys import argv
    if len(argv) < 4:
        print("Error: 3 arguments are required")
        sys.exit()
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine, orm)
    String = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(String.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = orm.sessionmaker(bind=engine)
    session = Session()
    state_add = State(name='Carlifornia')
    city_add = City(name='San Francisco', state=add_state)
    session.add(city_add)
    session.commit()
