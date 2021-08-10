from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class TiempoDedicacionProfesorSchema(BaseModel):
    id: str
    tiempo_dedicacion: str = Field(...)
    registrado_en: datetime
    actualizado_en: datetime


class TiempoDedicacionProfesorPostSchema(BaseModel):

    tiempo_dedicacion: str = Field(...)

    @validator("tiempo_dedicacion")
    def tiempo_dedicacion_maxima_longitud(cls, value):
        return longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "example": {
                "tiempo_dedicacion": "EXCLUVIVA O TIEMPO COMPLETO"
            }
        }


class TiempoDedicacionProfesorPutSchema(BaseModel):
    id: str = Field(...)
    tiempo_dedicacion: str = Field(...)

    @validator("tiempo_dedicacion")
    def tiempo_dedicacion_maxima_longitud(cls, value):
        longitud_maxima(50, value)
