#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Engine yaradılır
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Adında 'a' olan bütün ştatları tapırıq
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    # 2. Dövr (loop) qurub hər birini silirik
    for state in states_to_delete:
        session.delete(state)

    # 3. Dəyişiklikləri yadda saxlayırıq (COMMIT)
    session.commit()

    session.close()
