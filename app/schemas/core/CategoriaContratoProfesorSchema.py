
from datetime import datetime
from app.schemas.validaciones import longitud_maxima
from pydantic import BaseModel, Field, validator


class CategoriaContatoProfesorSchema(BaseModel):
    id: str
    categoria_contrato: str
    registrado_en: datetime
    actualizado_en: datetime


class CategoriaContratoProfesorPostSchema(BaseModel):
    categoria_contrato: str = Field(...)

    @validator("categoria_contrato")
    def categoria_contrato_maxima_longitud(cls, value):
        longitud_maxima(50, value)

    class Config:
        eschema_extra = {
            "ejemplo": {
                "categoria": "TITULAR PRINCIPAL"
            }
        }


class CategoriaContatoProfesorPutSchema(BaseModel):
    id: str = Field(...)
    categoria_contrato: str = Field(..., max_length=50)

    @validator("categoria_contrato")
    def categoria_contrato_maxima_longitud(cls, value):
        longitud_maxima(50, value)
