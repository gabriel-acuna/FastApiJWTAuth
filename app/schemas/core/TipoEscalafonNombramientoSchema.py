from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class TipoEscalafonNombramientoSchema(BaseModel):
    id: str
    escalafon_nombramiento: str
    registrado_en: datetime
    actualizado_en: datetime


class TipoEscalafonNombramientoPostSchema(BaseModel):
    escalafon_nombramiento: str = Field(...)

    @validator("escalafon_nombramiento")
    def escalafon_nombramiento_maxima_longitud(cls, value):
        return longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "example": {
                "escalafon_nombramiento": "LABORAL PREVIO"
            }
        }


class TipoEscalafonNombramientoPutSchema(BaseModel):
    id: str = Field(...)
    escalafon_nombramiento: str = Field(...)

    @validator("escalafon_nombramiento")
    def escalafon_nombramiento_maxima_longitud(cls, value):
        return longitud_maxima(50, value)