from typing import Optional
from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import longitud_maxima, es_no_numerico


class AreaInstitucionSchema(BaseModel):
    id: int
    nombre: str
    codigo: str


class AreaInstitucionalPutSachema(BaseModel):
    nombre: str = Field(...)
    codigo: Optional[str] = None

    @validator('nombre')
    def documento_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 3)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "id_estructura": 1,
                "nombre": "OCS"

            }
        }


class AreaInstitucionalPutSachema(BaseModel):
    id: int = Field(...)
    nombre: str = Field(...)
    codigo: Optional[str] = None

    @validator('nombre')
    def documento_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 3)
        if r and es_no_numerico(value):
            return value
