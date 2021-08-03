from sqlalchemy.dialects.postgresql.base import TIMESTAMP
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from app.models import Base
from sqlalchemy import Column, String, func
from sqlalchemy.dialects.postgresql import UUID
from app.models.async_crud import OperacionesLecturaAsincronas, OperacionesEscrituraAsinconas, EliminacionAsincrona

""" 
    Autor: Ing. Gabriel Acuña
    Descripción: Este módulo contiene los modelos asociados a los INSTRUCTIVO CARGA MASIVA SISTEMA
    DE INFORMACIÓN INTEGRAL DE LA EDUCACIÓN SUPERIOR Versión 6
"""


class Discapacidad(Base, OperacionesEscrituraAsinconas,
                   OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "discapacidades"
    id = Column(UUID, primary_key=True, index=True)
    discapacidad = Column(String(30), unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class Etnia(Base, OperacionesEscrituraAsinconas,
            OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "etnias"
    id = Column(UUID, primary_key=True, index=True)
    etnia = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class Nacionalidad(Base, OperacionesEscrituraAsinconas,
                   OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "nacionalidades"
    id = Column(UUID, primary_key=True, index=True)
    nacionalidad = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class TipoDocumento(Base, OperacionesEscrituraAsinconas,
                    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_documento"
    id = Column(UUID, primary_key=True, index=True)
    tipo_documento = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class RelacionIES(Base, OperacionesEscrituraAsinconas,
                  OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "relaciones_ies"
    id = Column(UUID, primary_key=True, index=True)
    relacion = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class TipoEscalafonNombramiento(Base, OperacionesEscrituraAsinconas,
                                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_relaciones_nombramientos"
    id = Column(UUID, primary_key=True, index=True)
    escalafon_nombramiento = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class CategoriaContratoProfesor(Base, OperacionesEscrituraAsinconas,
                                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "categorias_contratos_profesores"
    id = Column(UUID, primary_key=True, index=True)
    categoria_contrato = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class TiempoDedicacionProfesor(Base, OperacionesEscrituraAsinconas,
                               OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tiempo_dedicacion_profesores"
    id = Column(UUID, primary_key=True, index=True)
    tiempo_dedicacion = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class NivelEducativo(Base, OperacionesEscrituraAsinconas,
                     OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "nivel_educativo"
    id = Column(UUID, primary_key=True, index=True)
    nivel = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class TipoFuncioinario(Base, OperacionesEscrituraAsinconas,
                       OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipo_funcionarios"
    id = Column(UUID, primary_key=True, index=True)
    tipo = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,
                            onupdate=func.current_timestamp())


class TipoDocenteLOES(Base, OperacionesEscrituraAsinconas,
                      OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_docente_loes"
    id = Column(UUID, primary_key=True, index=True)
    tipo_docente = Column(String(50),nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,    onupdate=func.current_timestamp())


class CategoriaDocenteLOSEP(Base, OperacionesEscrituraAsinconas,
                            OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "categorias_docentes_losep"
    id = Column(UUID, primary_key=True, index=True)
    categoria_docente = Column(String(50), unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,    onupdate=func.current_timestamp())


class Pais(Base, OperacionesEscrituraAsinconas,
           OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "paises"
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String(120), nullable=False)
    nacionalidad = Column(String(120), nullable=True, default='')
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,    onupdate=func.current_timestamp())


class Provincia(Base, OperacionesEscrituraAsinconas,
                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "provincias"
    id = Column(Integer, primary_key=True, index=True)
    provincia = Column(String(120), nullable=False)
    cantones = relationship("Canton")
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,    onupdate=func.current_timestamp())


class Canton(Base, OperacionesEscrituraAsinconas,
             OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "cantones"
    id = Column(Integer, primary_key=True)
    canton = Column(String(120), nullable=False)
    provincia_id = Column(Integer, ForeignKey("provincias.id"))
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, nullable=True,    onupdate=func.current_timestamp())
