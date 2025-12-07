#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # 1. Engine yaradılır (Bazaya qoşulmaq üçün)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # 2. Session yaradılır (Sorğuları icra etmək üçün)
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3. Sorğu: Bütün State obyektlərini id-yə görə sıralayıb götürürük
    # SQL qarşılığı: SELECT * FROM states ORDER BY id ASC;
    states = session.query(State).order_by(State.id).all()

    # 4. Nəticələri çap edirik
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 5. Sessiyanı bağlayırıq
    session.close()
