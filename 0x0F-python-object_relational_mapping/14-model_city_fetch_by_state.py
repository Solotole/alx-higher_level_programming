#!/usr/bin/python3
"""script to retrieve data from 2 tables"""

if __name__ == '__main__':
    list_tuple = []
    from sys import exit, argv
    if len(argv) < 4:
        print("Error: moe arguments needed")
        exit()
    from sqlalchemy import orm, create_engine
    from model_state import Base, State
    from model_city import City
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = orm.sessionmaker(bind=engine)
    session = Session()
    lists_tuple = session.query(State, City) \
        .filter(City.state_id == State.id).order_by(City.id).all()
    for state, city in lists_tuple:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
