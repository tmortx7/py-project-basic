from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Sites(Base):
    __tablename__ = "sites"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    department_name = Column(String, ForeignKey('departments.name'))
    name = Column('name', String, unique=True)
    alias = Column('alias', String, unique=True)

class Departments(Base):
    __tablename__ = "departments"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, unique=True)
    alias = Column('alias', String, unique=True)
    #sites = relationship("Sites", back_populates="department_name")

engine = create_engine('sqlite:///db/dbfield.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def add_department(name, alias):
    session = Session()

    data = Departments()
    data.name = name
    data.alias = alias

    session.add(data)
    session.commit()
    session.close()

def query_allDepartments():
    session = Session()
    result = session.query(Departments).all()
    list = []
    for name in result:
        list.append([name.name ])
    session.close()
    return list

def add_site(department_name,name, alias):
    session = Session()

    data = Sites()
    data.department_name= department_name
    data.name = name
    data.alias = alias

    session.add(data)
    session.commit()
    session.close()