
from datetime import datetime
from app.schemas.validaciones import es_no_numerico, longitud_maxima
from pydantic import BaseModel, Field, validator


class EtniaSchema(BaseModel):
    id: str
    etnia: str
    registrado_en: datetime
    actualizado_en: datetime


class EtniaPostSchema(BaseModel):
    etnia: str = Field(...)

    @validator('etnia')
    def etnia_longitud_maxima(cls, value):
        r = longitud_maxima(30, value, 4)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "etnia": "INDIGENA"
            }
        }


class EtniaPutSchema(BaseModel):
    id: str = Field(...)
    etnia: str = Field(...)

    @validator('etnia')
    def etnia_longitud_maxima(cls, value):
        r = longitud_maxima(30, value, 4)
        if r and es_no_numerico(value):
            return value
