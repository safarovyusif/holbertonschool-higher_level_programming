#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
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

    # Sorğu: İlk obyekti götürürük (LIMIT 1)
    state = session.query(State).order_by(State.id).first()

    # Yoxlayırıq: Əgər baza boş deyilsə çap edirik, boşdursa "Nothing" yazırıq
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    
    session.close()
