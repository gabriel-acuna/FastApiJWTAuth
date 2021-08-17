from datetime import datetime
from app.models.core.modelos_principales import CategoriaDocenteLOSEP
from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import es_alafanumerico, longitud_maxima


class CategoriaDocenteLOSEPSchema(BaseModel):
    id: str
    categoria_docente: str
    registrado_en: datetime
    actualizado_en: datetime


class CategoriaDocenteLOSEPPostSchema(BaseModel):
    categoria_docente: str = Field(...)

    @validator("categoria_docente")
    def categoria_docente_validaciones(cls, value):
        r = longitud_maxima(50, value,11)
        if r and es_alafanumerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "categoria_docente": "CATEGORIA 1"
            }
        }


class CategoriaDocenteLOSEPPutSchema(BaseModel):
    id: str = Field(...)
    categoria_docente: str = Field(...)

    @validator("categoria_docente")
    def categoria_docente_validaciones(cls, value):
        r = longitud_maxima(50, value,11)
        if r and es_alafanumerico(value):
            return r

    class Config:
        schema_extra = {
            "example": {
                "id":"",
                "categoria_docente": ""
            }
        }