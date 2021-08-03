from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class TipoDocumentosSchema(BaseModel):
    id: str
    tipo_documento: str
    registrado_en: datetime
    actualizado_en: datetime


class TipoDocumentoPostSchema(BaseModel):
    tipo_documento: str = Field(...)

    @validator("tipo_documento")
    def tipo_documento_longitud_maxima(cls, value):
        longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "tipo_documento": {
                "tipo_documento": "CONTRATO"
            }
        }


class TipoDocumentoPutSchema(BaseModel):
    id: str = Field(...)
    tipo_documento: str = Field(...)

    @validator("tipo_documento")
    def tipo_documento_longitud_maxima(cls, value):
        longitud_maxima(50, value)
