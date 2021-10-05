from sqlalchemy.sql.elements import False_
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Enum, Date, Enum, Integer
from app.models import Base
from app.models.async_crud import *
from sqlalchemy import Column, String, func, text
from sqlalchemy.dialects.postgresql import UUID
import enum

""""
    Autor: Ing. Gabriel Acuña
    Descripción: Este módulo contiene los modelos relacionados con el cv del 
    personal que forma parte de la institucion
"""
class TipoCertificado(enum.Enum):
    ASISTENCIA = "ASISTENCIA"
    APROBACION = "APROBACIÓN"


class Capacitacion(Base,
    OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas,
    EliminacionAsincrona):
    __tablename__ = "capacitaciones"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey("datos_personales.identificacion"), nullable=False)
    tipo_evento = Column(String(30), nullable=False)
    institucion_organizadora = Column(String(80), nullable=False)
    lugar = Column(String(30), nullable=False)
    horas = Column(Integer, nullable=False)
    inicio = Column(Date, nullable=False)
    fin = Column(Date, nullable=False)
    tipo_certificado = Column(Enum(TipoCertificado))
    url_certificado = Column(String)


class TipoReferencia(enum.Enum):
    PERSONAL = "PERSONAL"
    LABORAL  = "LABORAL"

class Referencia(
    Base,
    OperacionesLecturaAsincronas,
    OperacionesEscrituraAsinconas,
    EliminacionAsincrona):
    __tablename__ = "referencias"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey("datos_personales.identificacion"), nullable=False)
    referencia = Column(Enum(TipoReferencia))
    apellidos = Column(String(80), nullable=False)
    nombres = Column(String(80), nullable=False)
    direccion = Column(String(120), nullable=False)
    correo_electronico = Column(String(80) )
    telefono_domicilio = Column(
        String(10), default="0000000000")
    telefono_movil = Column(String(13), nullable=False)
