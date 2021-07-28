from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from app.models import Base
from sqlalchemy import Column, String 
from sqlalchemy.dialects.postgresql import UUID

""" 
    Autor: Ing. Gabriel Acuña
    Descripción: Este módulo contiene los modelos asociados a los INSTRUCTIVO CARGA MASIVA SISTEMA
    DE INFORMACIÓN INTEGRAL DE LA EDUCACIÓN SUPERIOR Versión 6
"""


class Discapacidad(Base):
    __tablename__ = "discapacidades"
    id = Column(UUID, primary_key=True, index=True)
    discapacidad = Column(String(6), unique=True)

class Etnia(Base):
    __tablename__ = "etnias"
    id = Column(UUID, primary_key=True, index=True)
    etnia = Column(String(50),)

class Nacionalidad(Base):
    __tablename__ = "nacionalidades"
    id = Column(UUID, primary_key=True, index=True)
    nacionalidad = Column(String(50), unique=True)

class TipoDocumento(Base):
    __tablename__= "tipos_documento"
    id = Column(UUID, primary_key=True, index=True)
    tipo_documento = Column(String(50), unique=True)

class RelacionIES(Base):
    __tablename__ = "relaciones_ies"
    id = Column(UUID, primary_key=True, index=True)
    relacion = Column(String(50), unique=True)

class TipoEscalafonNombramiento(Base):
    __tablename__ = "tipos_relaciones_nombramientos"
    id = Column(UUID, primary_key=True, index=True)
    relacion_nombramiento = Column(String(50), unique=True)

class CategoriaContratoProfesor(Base):
    __tablename__ = "categorias_contratos_profesores"
    id = Column(UUID, primary_key=True, index=True)
    categoria_contrato = Column(String(50), unique=True)

class TiempoDedicacionProfesor(Base):
    __tablename__ = "tiempo_dedicacion_profesores"
    id = Column(UUID, primary_key=True, index=True)
    tiempo_dedicacion = Column(String(50), unique=True)

class NivelEducativo(Base):
    __tablename__ = "nivel_educativo"
    id = Column(UUID, primary_key=True, index=True)
    nivel = Column(String(50), unique=True)

class TipoFuncioinario(Base):
    __tablename__ = "tipo_funcionarios"
    id = Column(UUID, primary_key=True, index=True)
    tipo = Column(String(50), unique=True)


class TipoDocenteLOES(Base):
    __tablename__ = "tipos_docente_loes"
    id = Column(UUID, primary_key=True, index=True)
    tipo_docente = Column(String(50), unique=True)

class CategoriaDocenteLOSEP(Base):
    __tablename__  = "categorias_docentes_losep"
    id = Column(UUID, primary_key=True, index=True)
    categoria_docente = Column(String(50), unique=True)

class Pais(Base):
    __tablename__ = "paises"
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String(120))
    nacionalidad = Column(String(120), nullable=True, default='')