from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Data(Base):
    __tablename__ = "departments"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, unique=True)
    alias = Column('alias', String, unique=True)


engine = create_engine('sqlite:///dbfield.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def add_department(name, alias):
    session = Session()

    data = Data()
    data.name = name
    data.alias = alias

    session.add(data)
    session.commit()
    session.close()
