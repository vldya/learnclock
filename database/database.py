

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:password@localhost:5432/learn_clock')

Session = sessionmaker(engine)


def get_db_session() -> Session:
    return Session
