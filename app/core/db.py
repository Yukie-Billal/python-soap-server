from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://python_soap_server:xy-c(PQdwH3J1ZRN@localhost/python_soap_server")

_SessionFactory = sessionmaker(bind=engine)

BaseModel = declarative_base()

def session_factory():
    BaseModel.metadata.create_all(engine)
    return _SessionFactory()