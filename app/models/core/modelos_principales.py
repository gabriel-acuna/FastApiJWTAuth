from sqlalchemy.dialects.postgresql.base import TIMESTAMP
from sqlalchemy.sql.schema import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
from app.models import Base
from sqlalchemy import Column, String, func, text
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
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    discapacidad = Column(String(30), unique=True, nullable=False)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class Etnia(Base, OperacionesEscrituraAsinconas,
            OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "etnias"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    etnia = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class Nacionalidad(Base, OperacionesEscrituraAsinconas,
                   OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "nacionalidades"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    nacionalidad = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoDocumento(Base, OperacionesEscrituraAsinconas,
                    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_documento"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tipo_documento = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class RelacionIES(Base, OperacionesEscrituraAsinconas,
                  OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "relaciones_ies"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    relacion = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoEscalafonNombramiento(Base, OperacionesEscrituraAsinconas,
                                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_escalafones_nombramientos"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    escalafon_nombramiento = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class CategoriaContratoProfesor(Base, OperacionesEscrituraAsinconas,
                                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "categorias_contratos_profesores"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    categoria_contrato = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TiempoDedicacionProfesor(Base, OperacionesEscrituraAsinconas,
                               OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tiempo_dedicacion_profesores"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tiempo_dedicacion = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class NivelEducativo(Base, OperacionesEscrituraAsinconas,
                     OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "nivel_educativo"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    nivel = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoFuncionario(Base, OperacionesEscrituraAsinconas,
                      OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipo_funcionarios"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tipo = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(TIMESTAMP, server_default=func.now(),
                            onupdate=func.current_timestamp())


class TipoDocenteLOES(Base, OperacionesEscrituraAsinconas,
                      OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "tipos_docente_loes"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    tipo_docente = Column(String(50), nullable=False, unique=True)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class CategoriaDocenteLOSEP(Base, OperacionesEscrituraAsinconas,
                            OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "categorias_docentes_losep"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    categoria_docente = Column(String(50), unique=True, nullable=False)
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class Pais(Base, OperacionesEscrituraAsinconas,
           OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "paises"
    __table_args__ = (
        UniqueConstraint('pais', name='uc_pais'),
    )
    id = Column(Integer, primary_key=True, index=True)
    pais = Column(String(120), nullable=False)
    nacionalidad = Column(String(120), nullable=True, default='')
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class Provincia(Base, OperacionesEscrituraAsinconas,
                OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "provincias"
    __table_args__ = (
        UniqueConstraint('provincia', name='uc_provincia'),
    )

    id = Column(Integer, primary_key=True, index=True)
    provincia = Column(String(120), nullable=False)
    cantones = relationship("Canton")
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class Canton(Base, OperacionesEscrituraAsinconas,
             OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "cantones"
    __table_args__ = (
        UniqueConstraint('canton', 'provincia_id', name='uc_canton_provincia'),
    )
    id = Column(Integer, primary_key=True)
    canton = Column(String(120), nullable=False)
    provincia_id = Column(Integer, ForeignKey("provincias.id"))
    registrado_en = Column(TIMESTAMP, server_default=func.now())
    actualizado_en = Column(
        TIMESTAMP, server_default=func.now(),    onupdate=func.current_timestamp())


class EstadoCivil(Base, OperacionesEscrituraAsinconas, OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "estados_civiles"
    id = Column(Integer, primary_key=True)
    estado_civil = Column(String(30), nullable=False)


class EstructuraInstucional(Base, OperacionesEscrituraAsinconas, OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "estructura_organica_institucional"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(80), nullable=False)
    codigo = Column(String(50), default='')
    id_area = Column(Integer, default=0)
