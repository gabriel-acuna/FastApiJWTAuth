
from datetime import datetime
from app.schemas.validaciones import longitud_maxima
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
        longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "etnia": {
                "etnia": "INDIGENA"
            }
        }


class EtniaPostSchema(BaseModel):
    id: str = Field(...)
    etnia: str = Field(...)

    @validator('etnia')
    def etnia_longitud_maxima(cls, value):
        longitud_maxima(50, value)
