from sqlalchemy.sql.expression import false
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Enum, Date, Enum, Integer, Numeric
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


class EstadoFormacion(enum.Enum):
    TERMINADA = "FINALIZADO"
    CURSANDO = "EN CURSO"


class FormacionAcademica(Base, OperacionesEscrituraAsinconas, EliminacionAsincrona):
    __tablename__ = "formacion_academica_personal"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    id_pais_estudio = Column(ForeignKey("paises.id"), nullable=False)
    id_ies = Column(ForeignKey("ies_nacionales.id"))
    nombre_ies = Column(String(150))
    id_nivel = Column(ForeignKey('nivel_educativo.id'), nullable=False)
    id_grado = Column(ForeignKey('grados.id'))
    nombre_titulo = Column(String(150), nullable=False)
    id_campo_detallado = Column(ForeignKey(
        'campo_educativo_detallado.id'), nullable=False)
    estado = Column(Enum(EstadoFormacion), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)
    registro_senescyt = Column(String(20))
    fecha_obtencion_titulo = Column(Date)
    lugar = Column(String(120), nullable=False)
    posee_beca = Column(String(2))
    id_tipo_beca = Column(ForeignKey('tipo_beca.id'))
    monto_beca = Column(Numeric(8, 2), default=0)
    id_financiamiento = Column(ForeignKey('financiamiento_beca.id'))
    descripcion = Column(String(100))


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
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    tipo_evento = Column(String(30), nullable=False)
    institucion_organizadora = Column(String(80), nullable=False)
    lugar = Column(String(30), nullable=False)
    horas = Column(Integer, nullable=False)
    inicio = Column(Date, nullable=False)
    fin = Column(Date, nullable=False)
    tipo_certificado = Column(Enum(TipoCertificado))
    url_certificado = Column(String)


class CapacitacionFacilitador(Base,
    OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas, EliminacionAsincrona):
    __tablename__ = "capacitaciones_facilitadores"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    funcion_evento = Column(String(75), nullable=False)
    institucion_organizadora = Column(String(80), nullable=False)
    lugar = Column(String(120), nullable=False)
    horas = Column(Integer, nullable=False)
    inicio = Column(Date, nullable=False)
    fin = Column(Date, nullable=False)
    certificado = Column(String(120))


class Ponencia(Base,
    OperacionesLecturaAsincronas,
    OperacionesEscrituraAsinconas,
    EliminacionAsincrona
    ):
    __tablename__ = "ponencias_exposiciones"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    tema = Column(String(150), nullable=False)
    institucion_organizadora = Column(String(80), nullable=False)
    evento = Column(String(120), nullable=False)
    caracter = Column(String(13), nullable=False)
    lugar = Column(String(120))
    fecha = Column(Date, nullable=False)


class ExperienciaLaboral(Base,
    OperacionesLecturaAsincronas,
    OperacionesEscrituraAsinconas,
    EliminacionAsincrona):
    __tablename__ = "experiencia_laboral_personal"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text('uuid_generate_v4()'))
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    empresa = Column(String(120), nullable=False)
    lugar = Column(String(120), nullable=False)
    cargo = Column(String(60), nullable=False)
    inicio = Column(Date, nullable=False)
    fin = Column(Date)


class MeritoDistincion(Base,
    OperacionesEscrituraAsinconas,
    OperacionesLecturaAsincronas,
    EliminacionAsincrona):
    __tablename__ = 'meritos_distinciones'
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    titulo = Column(String(130), nullable=False)
    institucion_auspiciante = Column(String(130), nullable=False)
    funcion = Column(String(80), nullable=False)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date)


class NivelComprension(enum.Enum):
    Excelente = 'Excelente'
    Buena = 'Buena'
    Limitada = 'Limitada'
    Ninguna = 'Ninguna'


class ComprensionIdioma(Base,
    OperacionesLecturaAsincronas,
    OperacionesEscrituraAsinconas,
    EliminacionAsincrona):
    __tablename__ = 'comprension_idiomas'
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    idioma = Column(String(30), nullable=False)
    lugar_estudio = Column(String(120), nullable=False)
    nivel_comprension = Column(Enum(NivelComprension), nullable=False)


class TipoReferencia(enum.Enum):
    PERSONAL = "PERSONAL"
    LABORAL = "LABORAL"


class Referencia(
        Base,
        OperacionesLecturaAsincronas,
        OperacionesEscrituraAsinconas,
        EliminacionAsincrona):
    __tablename__ = "referencias"
    id = Column(UUID, primary_key=True, index=True,
                server_default=text("uuid_generate_v4()"))
    id_persona = Column(ForeignKey(
        "datos_personales.identificacion"), nullable=False)
    referencia = Column(Enum(TipoReferencia))
    apellidos = Column(String(80), nullable=False)
    nombres = Column(String(80), nullable=False)
    direccion = Column(String(120), nullable=False)
    correo_electronico = Column(String(80))
    telefono_domicilio = Column(
        String(10), default="0000000000")
    telefono_movil = Column(String(13), nullable=False)
