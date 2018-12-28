from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import parameters
import pandas as pd


db_string = "postgresql://{0}:{1}@{2}:{3}/{4}"


def getClutchDbConfig():
    return db_string.format(os.environ.get('PGS_USERNAME'),os.environ.get('PGS_PASSWORD'),os.environ.get('PGS_HOST'),os.environ.get('PGS_PORT', 5432),os.environ.get('PGS_DB'))

engine_db = create_engine(getClutchDbConfig(), convert_unicode=True)

def prod_db():
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine_db))
    return db_session

