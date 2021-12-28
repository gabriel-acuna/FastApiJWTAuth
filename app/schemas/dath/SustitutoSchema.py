from pydantic import BaseModel, Field
import enum
from datetime import date

class TipoSustituto(str, enum.Enum):
    DIRECTO = 'DIRECTO'
    SOLIDADRIDAD = 'SOLIDARIDAD'

class SustitutoSchema(BaseModel):
    id:str
    id_persona:str
    tipo_sustituto: TipoSustituto
    apellidos:str
    nombres:str
    numero_carnet: str
    desde:date
    hasta: date

class SustitutoPostSchema(BaseModel):
    id_persona:str = Field(...)
    tipo_sustituto: TipoSustituto = Field(...)
    apellidos:str = Field(...)
    nombres:str = Field(...)
    numero_carnet: str = Field(...)
    desde:date = Field(...)
    hasta: date = Field(...)

class SustitutoPutSchema(BaseModel):
    id:str = Field(...)
    tipo_sustituto: TipoSustituto = Field(...)
    apellidos:str = Field(...)
    nombres:str = Field(...)
    numero_carnet: str = Field(...)
    desde:date = Field(...)
    hasta: date = Field(...)