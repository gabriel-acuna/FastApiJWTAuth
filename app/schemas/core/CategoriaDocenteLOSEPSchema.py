from datetime import datetime
from app.models.core.modelos_principales import CategoriaDocenteLOSEP
from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import longitud_maxima


class CategoriaDocenteLOSEPSchema(BaseModel):
    id: str
    categoria_docente: str
    registrado_en: datetime
    actualizado_en: datetime


class CategoriaDocenteLOSEPPostSchema(BaseModel):
    categoria_docente: str = Field(...)

    @validator("categoria_docente")
    def categoria_docente_maxima_longitud(cls, value):
        longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "ejemplo": {
                "tipo": "ADMINISTRATIVO"
            }
        }


class CategoriaDocenteLOSEPPostSchema(BaseModel):
    id: str = Field(...)
    categoria_docente: str = Field(...)

    @validator("categoria_docente")
    def categoria_docente_maxima_longitud(cls, value):
        longitud_maxima(50, value)
