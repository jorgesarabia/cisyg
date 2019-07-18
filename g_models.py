"""
El usuario va ser central en la aplicación, asi que creo que se lo 
puede poner como un modelo 'global'
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

if __name__ == "__main__":
    pass

"""
import os
import time
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ciudad(Base):
    __tablename__ = "ciudades"
    id = Column(Integer, primary_key=True)
    recurso = Column(Integer,ForeignKey('recursos.id'))
    nombre = Column(String)

    recursos = relationship('RecursosCiudades', backref='recursos_ciudad')

    def __repr__(self):
        return "<Ciudad(nombre='{}', recurso='{}')>".format(self.nombre, self.recurso)


class Recursos(Base):
    __tablename__ = "recursos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)

    ciudades = relationship('Ciudad', backref='ciudades')
    recursos_ciudades = relationship('RecursosCiudades', backref='recursos_ciudades')

    def __repr__(self):
        return "<Recursos(nombre='{}')>".format(self.nombre)


class RecursosCiudades(Base):
    __tablename__ = "recursos_ciudad"
    id = Column(Integer, primary_key=True)
    ciudad = Column(Integer,ForeignKey('ciudades.id'))
    recurso = Column(Integer,ForeignKey('recursos.id'))
    cantidad = Column(Integer)

    city = relationship('Ciudad', backref='nombre_ciudad')
    resource = relationship('Recursos')

    def __repr__(self):
        return "<Recursos(ciudad='{}', recurso='{}', cantidad='{}')>"\
        .format(self.ciudad, self.recurso, self.cantidad)


class EdificioEnContruccion(Base):
    __tablename__ = "edificio_en_construccion"
    id = Column(Integer, primary_key=True)
    finaliza = Column(Float)
    ciudad = Column(Integer,ForeignKey('ciudades.id'))

    city = relationship('Ciudad')

    def __repr__(self):
        return "<Edificios en construccion(ciudad='{}', finaliza='{}')>"\
        .format(self.city.nombre, time.ctime(self.finaliza))


class ListaConstruccion(Base):
    __tablename__ = "lista_construccion"
    id = Column(Integer, primary_key=True)
    ciudad = Column(Integer,ForeignKey('ciudades.id'))
    edificio = Column(Integer,ForeignKey('edificios.id'))

    building = relationship('Edificios')
    city = relationship('Ciudad')

    def __repr__(self):
        return "<Lista de construccion(ciudad='{}', edificio='{}')>"\
        .format(self.ciudad, self.edificio)


class Edificios(Base):
    __tablename__ = "edificios"
    id = Column(Integer, primary_key=True)
    ciudad = Column(Integer,ForeignKey('ciudades.id'))
    nombre = Column(String)
    id_html = Column(String)
    nivel = Column(Integer)

    city = relationship('Ciudad', backref='nomb_ciudad')

    def __repr__(self):
        return "<Edificios(ciudad='{}', edificio='{}', nivel='{}')>"\
        .format(self.city.nombre, self.nombre, self.nivel)


class ProximoNivel(Base):
    __tablename__ = "proximo_nivel"
    id = Column(Integer, primary_key=True)
    recurso = Column(Integer,ForeignKey('recursos.id'))
    edificio = Column(Integer,ForeignKey('edificios.id'))
    cantidad = Column(Integer)

    building = relationship('Edificios')
    resource = relationship('Recursos')

    def __repr__(self):
        return "<Proximo Nivel(ciudad='{}',edificio='{}', recurso='{}', cantidad='{}')>"\
        .format(self.building.city.nombre, self.building.nombre, self.resource.nombre, self.cantidad)


if __name__ == "__main__":
    db_name = 'ikadb.sqlite'
    if os.path.exists(db_name):
        os.remove(db_name)
    
    engine = create_engine('sqlite:///' + db_name)
    Base.metadata.create_all(engine)

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    #Ciudades:
    session.add(Ciudad(nombre="PoVi",   recurso=2))
    session.add(Ciudad(nombre="PoMa",   recurso=3))
    session.add(Ciudad(nombre="PoAz",   recurso=5))
    session.add(Ciudad(nombre="PoCr",   recurso=4))
    session.add(Ciudad(nombre="PoMaII", recurso=3))
    session.add(Ciudad(nombre="Pomalll",recurso=3))
    session.add(Ciudad(nombre="PoVill", recurso=2))
    session.add(Ciudad(nombre="P2P",    recurso=3))
    session.add(Ciudad(nombre="PVC",    recurso=2))
    session.add(Ciudad(nombre="Polis",  recurso=4))

    #Recursos:
    session.add(Recursos(nombre="wood"))# 1
    session.add(Recursos(nombre="wine"))# 2
    session.add(Recursos(nombre="marble"))# 3
    session.add(Recursos(nombre="crystal"))# 4
    session.add(Recursos(nombre="sulfur"))# 5

    session.commit()
"""
