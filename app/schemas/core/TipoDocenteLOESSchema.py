from datetime import datetime
from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import es_no_numerico, longitud_maxima


class TipoDocenteLOESSchema(BaseModel):
    id: str
    tipo_docente: str
    registrado_en: datetime
    actualizado_en: datetime


class TipoDocenteLOESPostSchema(BaseModel):
    tipo_docente: str = Field(...)

    @validator("tipo_docente")
    def tipo_docente_validaciones(cls, value):
        r  = longitud_maxima(50, value,7)
        if  r and  not es_no_numerico(value) :
            return value

   

    
    class Config:
        schema_extra = {
            "example": {
                "tipo_docente": "TECNICO DOCENTE"
            }
        }


class TipoDocenteLOESPutSchema(BaseModel):
    id: str = Field(...)
    tipo_docente: str = Field(...)

    @validator("tipo_docente")
    def tipo_docente_validaciones(cls, value):
        r  = longitud_maxima(50, value,7)
        if  r and  not es_no_numerico(value):
            return value
