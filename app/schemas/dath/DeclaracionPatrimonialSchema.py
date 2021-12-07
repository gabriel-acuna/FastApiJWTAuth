from pydantic import BaseModel, Field
import enum
from datetime import date

from app.schemas.dath.InformacionPersonalSchema import InformacionPersonalBasicaSchema


class TipoDeclaracion(str, enum.Enum):
    inicio = 'INICIO DE GESTION'
    periodica = 'PERIODICA'
    fin = 'FIN DE GESTION'


class DeclaracionPatrimonialDetalladaSchema(BaseModel):
    id: str
    persona: InformacionPersonalBasicaSchema
    tipo_declaracion: TipoDeclaracion
    numero_declaracion: str
    fecha_presentacion: date


class DeclaracionPatrimonialSchema(BaseModel):
    id: str
    persona: str
    tipo_declaracion: TipoDeclaracion
    numero_declaracion: str
    fecha_presentacion: date


class DeclaracionPatrimonialPostSchema(BaseModel):
    persona: str = Field(...)
    tipo_declaracion: TipoDeclaracion = Field(...)
    numero_declaracion: str = Field(...)
    fecha_presentacion: date = Field(...)


class DeclaracionPatrimonialPutSchema(BaseModel):
    id: str = Field(...)
    tipo_declaracion: TipoDeclaracion = Field(...)
    numero_declaracion: str = Field(...)
    fecha_presentacion: date = Field(...)
