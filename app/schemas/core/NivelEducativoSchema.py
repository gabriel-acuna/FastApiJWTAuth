from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class NivelEducativoSchema(BaseModel):
    id: str
    nivel: str
    registrado_en: datetime
    actualiado_en: datetime


class NivelEducativoPostSchema(BaseModel):
    nivel: str = Field(...)

    @validator("nivel")
    def tiempo_dedicacion_maxima_longitud(cls, value):
        longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "nivel_educativo": {
                "nivel": "TERCER NIVEL"
            }
        }


class NivelEducativoPutSchema(BaseModel):
    nivel: str = Field(...)

    @validator("nivel")
    def tiempo_dedicacion_maxima_longitud(cls, value):
        longitud_maxima(50, value)
