from enum import unique
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class PlantOwner(Base):
    __tablename__ = "plant_owner"

    owner = Column('owner', String,unique=True, primary_key=True)
    note = Column('note', String)
    plants = relationship("Plant", back_populates="owner")


class Plant(Base):
    __tablename__ = 'plant'

    plant = Column('plant', String, unique=True,primary_key=True)
    number = Column('number', String, unique=True)
    description = Column('description', String)
    note = Column('note', String)
    plant_owner_owner = Column(String, ForeignKey('plant_owner.owner'))
    owner = relationship("PlantOwner", back_populates="plants")
    address = relationship("Address", back_populates="plant")
    areas = relationship("PlantArea", back_populates="plant")


class PlantArea(Base):
    __tablename__ = 'plant_area'

    area = Column('area', String, primary_key=True)
    number = Column('number', String)
    description = Column('description', String)
    plant_plant = Column(String, ForeignKey('plant.plant'))
    plant = relationship("Plant", back_populates="areas")
    units = relationship("PlantUnit", back_populates="area")


class PlantUnit(Base):
    __tablename__ = 'plant_unit'

    unit = Column('unit', String, primary_key=True)
    number = Column('number', String, nullable=False)
    plant_area_area = Column(String, ForeignKey('plant_area.area'))
    area = relationship("PlantArea", back_populates="units")


class Address(Base):
    __tablename__ = 'address'

    plus_code = Column('plus_code', String, primary_key=True)
    plant_plant = Column(String, ForeignKey('plant.plant'))
    plant = relationship("Plant", back_populates="address")


class ProcessFunction(Base):
    __tablename__ = 'process_function'

    function = Column('function', String, primary_key=True)
    note = Column('note', String)
    instrument_types = relationship(
        "InstrumentType", back_populates="processfunction")


class InstrumentType(Base):
    __tablename__ = 'instrument_type'

    type = Column('type', String, primary_key=True)
    description = Column('description', String)
    process_function = Column(String, ForeignKey('process_function.function'))
    processfunction = relationship(
        "ProcessFunction", back_populates="instrument_types")


class InstrumentStatus(Base):
    __tablename__ = 'instrument_status'

    status = Column('status', String, primary_key=True)
    description = Column('description', String)


class InstrumentManufacturer(Base):
    __tablename__ = 'instrument_manufacturer'

    manufacturer = Column('manufacturer', String, primary_key=True)
    description = Column('description', String)


engine = create_engine('sqlite:///db/dbfield.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def add_owner(owner, note):
    session = Session()

    data = PlantOwner()
    data.owner = owner
    data.note = note

    session.add(data)
    session.commit()
    session.close()

def query_allOwners():
    session = Session()
    result = session.query(PlantOwner).all()
    list = []
    for owner in result:
        list.append([owner.owner])
    session.close()
    return list

def add_plant(plant,number,description,note,owner):
    session = Session()

    data = Plant()
    data.plant = plant
    data.number = number
    data.description = description
    data.note = note
    data.plant_owner_owner = owner

    session.add(data)
    session.commit()
    session.close()

def add_address(plus_code,plant_plant):
    session = Session()

    data = Address()
    data.plus_code = plus_code
    data.plant_plant = plant_plant


    session.add(data)
    session.commit()
    session.close()