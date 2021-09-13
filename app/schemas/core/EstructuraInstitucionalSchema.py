from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import longitud_maxima


class EstructuraInstitucionalSchema(BaseModel):
    id: int
    documento_aprobacion: str
    fecha_aprobacion: str


class EstructuraInstitucionalPostSchema(BaseModel):
    documento_aprobacion: str = Field(...)
    fecha_aprobacion: str = Field(...)

    @validator('documento_aprobacion')
    def documento_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 8)
        if r:
            return value

    @validator('fecha_aprobacion')
    def fecha_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 8)
        if r:
            return value

    class Config:
        schema_extra = {
            "example": {
                "documento_aprobacion": "RESOLUCION No. 024-01-2020",
                "fecha_aprobacion": "30 DE SEPTIEMBRE DE 2020"

            }
        }


class EstructuraInstitucionalPutSchema(BaseModel):
    id: int
    documento_aprobacion: str = Field(...)
    fecha_aprobacion: str = Field(...)

    @validator('documento_aprobacion')
    def documento_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 8)
        if r:
            return value

    @validator('fecha_aprobacion')
    def fecha_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 8)
        if r:
            return value

