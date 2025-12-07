#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
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

    # Sorğu: Adı arqumentə bərabər olan ştatı axtarırıq
    # SQL Injection-dan qorunmaq üçün SQLAlchemy avtomatik təmizləmə edir
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Nəticəni yoxlayırıq
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
