from datetime import datetime
from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import longitud_maxima, es_no_numerico


class TipoFuncionarioSchema(BaseModel):
    id: str
    tipo: str
    registrado_en: datetime
    actualizado_en: datetime


class TipoFuncionarioPostSchema(BaseModel):
    tipo: str = Field(...)

    @validator("tipo")
    def tipo_funcionario_maxima_longitud(cls, value):
        r = longitud_maxima(50, value, 9)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "tipo": "ADMINISTRATIVO"
            }
        }


class TipoFuncionarioPutSchema(BaseModel):
    id: str = Field(...)
    tipo: str = Field(...)

    @validator("tipo")
    def tipo_funcionario_maxima_longitud(cls, value):
        r = longitud_maxima(50, value, 9)
        if r and es_no_numerico(value):
            return value
