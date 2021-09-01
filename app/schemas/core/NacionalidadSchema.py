from datetime import datetime
from app.schemas.validaciones import es_no_numerico, longitud_maxima
from pydantic import BaseModel, Field, validator


class NacionalidadSchema(BaseModel):
    id: str
    nacionalidad: str
    registrado_en: datetime
    actualizado_en: datetime


class NacionalidadPostSchema(BaseModel):
    nacionalidad: str = Field(...)

    @validator('nacionalidad')
    def nacionalidad_longitud_maxima(cls, value):
        r = longitud_maxima(30, value, 3)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "nacionalidad": "TSACHILA"
            }
        }


class NacionalidadPutSchema(BaseModel):
    id: str = Field(...)
    nacionalidad: str = Field(...)

    @validator('nacionalidad')
    def nacionalidad_longitud_maxima(cls, value):
        r = longitud_maxima(30, value, 3)
        if r and es_no_numerico(value):
            return value
