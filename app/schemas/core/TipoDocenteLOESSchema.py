from datetime import datetime
from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import longitud_maxima


class TipoDocenteLOESSchema(BaseModel):
    id: str
    tipo_docente: str
    registrado_en: datetime
    actualizado_en: datetime


class TipoDocenteLOESPostSchema(BaseModel):
    tipo_docente: str = Field(...)

    @validator("tipo_docente")
    def tipo_docente_maxima_longitud(cls, value):
        return longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "example": {
                "tipo": "TECNICO DOCENTE"
            }
        }


class TipoDocenteLOESPutSchema(BaseModel):
    id: str = Field(...)
    tipo_docente: str = Field(...)

    @validator("tipo_docente")
    def tipo_docente_maxima_longitud(cls, value):
        return longitud_maxima(50, value)
