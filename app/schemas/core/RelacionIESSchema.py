from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class RelacionIESSchema(BaseModel):
    id: str
    relacion: str
    registrado_en: datetime
    actualizado_en: datetime


class RelacionIESPostSchema(BaseModel):
    relacion: str = Field(...)

    @validator('relacion')
    def relacion_longitud_maxima(cls, value):
        longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "relacion_ies": {
                "relacion": "NOMBRAMIENTO"
            }
        }


class RelacionIESPutSchema(BaseModel):
    id: str = Field(...)
    relacion: str = Field(...)

    @validator('relacion')
    def relacion_longitud_maxima(cls, value):
        longitud_maxima(50, value)
