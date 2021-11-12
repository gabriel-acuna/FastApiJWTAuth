from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from decouple import config
from sqlalchemy.sql import base
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Numeric, String
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine(config("DATABASE_URL_MIGRATIONS"),
                       echo=True)

Base = declarative_base(engine)


def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class PeriodoAcademico(Base):
    '''Modelo que permitirá consultar los periodos académicos registrados en el SGA'''
    id = Column(Integer, primary_key=true)
    __tablename__ = 'sga_periodo'
    __table_args__ = {'autoload': True, 'schema': 'sga'}


class Persona(Base):
    '''Modelo que permitirá aceder a información personal de profesores y estudiantes registrados en el SGA'''
    id = Column(Integer, primary_key=true)
    cedula = Column(String)
    pasaporte = Column(String)
    nombres = Column(String)
    apellido1 = Column(String)
    apellido2 = Column(String)

    profesor = relationship("Profesor", uselist=False)
    __tablename__ = 'sga_persona'
    __table_args__ = {'schema': 'sga'}


class Profesor(Base):
    '''Modelo  que permitirá consultar información de los profesore registrados en el SGA'''
    id = Column(Integer, primary_key=true)
    persona_id = Column(ForeignKey('sga.sga_persona.id'))
    __tablename__ = 'sga_profesor'
    __table_args__ = {'autoload': True, 'schema': 'sga'}


class Coordinacion(Base):
    id = Column(Integer, primary_key=true)
    __tablename__ = 'sga_coordinacion'
    __table_args__ = {'autoload': True, 'schema': 'sga'}


class ProfesorDistributivoHoras(Base):
    '''Modelo que permitira consultar el distributivo de horas de los profesores por periodo académico'''
    id = Column(Integer, primary_key=true)
    periodo_id = Column(ForeignKey('sga.sga_periodo'))
    profesor_id = Column(ForeignKey('sga.sga_profesor'))
    coordinacion = Column(ForeignKey('sga.sga_coordinacion'))
    horas = Column(Numeric(4, 2), default=0)
    horasdocencia = Column(default=0)
    horasinvestigacion = Column(Numeric(4, 2), default=0)
    horasgestion = Column(Numeric(4, 2), default=0,)
    horasvinculacion = Column(Numeric(4, 2), default=0)
    horaspracticas = Column(Numeric(4, 2), default=0)
    horasotrasactividades = Column(Numeric(4, 2), default=0)
    __tablename__ = 'sga_profesordistributivohoras'
    __table_args__ = {'autoload': True, 'schema': 'sga'}

    class CriterioDocenciaPeriodo(Base):
        id = Column(Integer, primary_key=true)
        __tablename__ = "sga_criteriodocenciaperiodo"
        __table_args__ = {'autoload': True, 'schema': 'sga'}

    class CriterioInvestigacionPeriodo(Base):
        id = Column(Integer, primary_key=true)
        __tablename__ = "sga_criterioinvestigacionperiodo"
        __table_args__ = {'autoload': True, 'schema': 'sga'}
    

    class CriterioGestionPeriodo(Base):
        id = Column(Integer, primary_key=true)
        __tablename__ = 'sga_criteriogestionperiodo'
        __table_args__ = {'autoload': True, 'schema': 'sga'}
        id=Column(Integer, primary_key=true)
        
    class CriterioVinculacionPeriodo(Base):
        id = Column(Integer, primary_key=true)
        __tablename__ = 'sga_criteriovinculacionperiodo'
        __table_args__ = {'autoload': True, 'schema': 'sga'}
        id=Column(Integer, primary_key=true)

    
    class CriterioPracticasPeriodo(Base):
        id = Column(Integer, primary_key=true)
        __tablename__ = 'sga_criteriopracticasperiodo'
        __table_args__ = {'autoload': True, 'schema': 'sga'}
        id=Column(Integer, primary_key=true)

    class CriterioOtrasActividadesPeriodo(Base):
        id = Column(Integer, primary_key=true)
        __tablename__ = 'sga_criteriootrasactividadesperiodo'
        __table_args__ = {'autoload': True, 'schema': 'sga'}
        id=Column(Integer, primary_key=true)

        criteriodocenciaperiodo_id = Column(ForeignKey('sga.criteriodocenciaperiodo_id'))
        criterioinvestigacionperiodo = Column(ForeignKey('sga.sga_criterioinvestigacionperiodo.id'))
        criteriogestionperiodo = Column(ForeignKey('sga.sga_criteriogestionperiodo.id'))
        criteriovinculacionperiodo = Column(ForeignKey('sga.criteriovinculacionperiodo.id'))
        criteriopracticasperiodo = Column(ForeignKey('sga.criteriopracticasperiodo.id'))
        criteriootrasactividadesperiodo = ForeignKey('sga.criteriootrasactividadesperiodo.id')
        horas = Column(Numeric(4,2), default=0)
