#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # Yeni obyekt yaradılır
    new_state = State(name="Louisiana")

    # Obyekt sessiyaya əlavə edilir
    session.add(new_state)

    # Dəyişikliklər bazaya yazılır (COMMIT)
    session.commit()

    # Yeni yaranan ID çap edilir
    print(new_state.id)

    session.close()
