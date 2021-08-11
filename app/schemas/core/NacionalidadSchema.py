from datetime import datetime
from app.schemas.validaciones import longitud_maxima
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
        return longitud_maxima(50, value)

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
        return longitud_maxima(50, value)
