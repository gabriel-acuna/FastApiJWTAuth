from datetime import datetime
from app.schemas.validaciones import longitud_maxima, es_no_numerico
from pydantic import BaseModel, Field, validator


class TipoDocumentoSchema(BaseModel):
    id: str
    tipo_documento: str
    registrado_en: datetime
    actualizado_en: datetime


class TipoDocumentoPostSchema(BaseModel):
    tipo_documento: str = Field(...)

    @validator("tipo_documento")
    def tipo_documento_longitud_maxima(cls, value):
        r = longitud_maxima(30, value, 7)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "tipo_documento": "CONTRATO"
            }
        }


class TipoDocumentoPutSchema(BaseModel):
    id: str = Field(...)
    tipo_documento: str = Field(...)

    @validator("tipo_documento")
    def tipo_documento_longitud_maxima(cls, value):
        r = longitud_maxima(30, value, 7)
        if r and es_no_numerico(value):
            return value
