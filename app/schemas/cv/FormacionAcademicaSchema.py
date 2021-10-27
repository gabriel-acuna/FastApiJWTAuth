from typing import Optional
from pydantic import BaseModel, Field
import enum
from app.schemas.core.PaisSchema import PaisSchema
from app.schemas.core.IESNacionalSchema import IESNacionalSchema
from app.schemas.core.NivelEducativoSchema import NivelEducativoSchema
from app.schemas.core.GradoSchema import GradoSchema
from app.schemas.core.CampoEducativoSchema import CampoEducativoDetalladoSchema
from datetime import date
from app.schemas.core.TipoBecaSchema import TipoBecaSchema
from app.schemas.core.FinanciamientoBecaSchema import FinanciamientoBecaSchema


class EstadoFormacion(str, enum.Enum):
    TERMINADA = "FINALIZADO"
    CURSANDO = "EN CURSO"


class FormacionAcademicaSchema(BaseModel):
    id: str
    id_persona: str
    pais_estudio: PaisSchema
    ies: Optional[IESNacionalSchema]
    nombre_ies: Optional[str]
    nivel_educativo: NivelEducativoSchema
    grado: Optional[GradoSchema]
    nombre_titulo: str
    campo_detallado: CampoEducativoDetalladoSchema
    estado: EstadoFormacion
    fecha_inicio: date
    fecha_fin: Optional[date]
    registro_senescyt: Optional[str]
    fecha_obtencion_titulo: Optional[date]
    lugar: str
    posee_beca: str
    tipo_beca: Optional[TipoBecaSchema]
    monto_beca: Optional[float]
    financiamiento: Optional[FinanciamientoBecaSchema]
    descripcion: Optional[str]


class FormacionAcademicaPostSchema(BaseModel):
    id_persona: str = Field(...)
    pais_estudio: str = Field(...)
    ies: Optional[str] = Field()
    nombre_ies: Optional[str] = Field()
    nivel_educativo: str = Field(...)
    grado: Optional[str] = Field()
    nombre_titulo: str = Field(...)
    campo_detallado: str = Field(...)
    estado: EstadoFormacion = Field(...)
    fecha_inicio: date = Field(...)
    fecha_fin: Optional[date] = Field()
    registro_senescyt: Optional[str] = Field()
    fecha_obtencion_titulo: Optional[date] = Field()
    lugar: str = Field(...)
    posee_beca: Optional[str] = Field()
    tipo_beca: Optional[str] = Field()
    monto_beca: Optional[float] = Field()
    financiamiento: Optional[str] = Field()
    descripcion: Optional[str] = Field()


class FormacionAcademicaPutSchema(BaseModel):
    id: str = Field(...)
    pais_estudio: str = Field(...)
    ies: Optional[str] = Field()
    nombre_ies: Optional[str] = Field()
    nivel_educativo: str = Field(...)
    grado: Optional[str] = Field()
    nombre_titulo: str = Field(...)
    campo_detallado: str = Field(...)
    estado: EstadoFormacion = Field(...)
    fecha_inicio: date = Field(...)
    fecha_fin: Optional[date] = Field()
    registro_senescyt: Optional[str] = Field()
    fecha_obtencion_titulo: Optional[date] = Field()
    lugar: str = Field(...)
    posee_beca: Optional[str] = Field()
    tipo_beca: Optional[str] = Field()
    monto_beca: Optional[float] = Field()
    financiamiento: Optional[str] = Field()
    descripcion: Optional[str] = Field()
