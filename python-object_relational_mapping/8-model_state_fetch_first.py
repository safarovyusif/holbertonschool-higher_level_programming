#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Bazaya qoşulma məlumatları
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Engine yaradılır
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, password, db_name), pool_pre_ping=True)

    # Session yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sorğu: İlk obyekti götürürük
    state = session.query(State).order_by(State.id).first()

    # Nəticəni yoxlayırıq
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
