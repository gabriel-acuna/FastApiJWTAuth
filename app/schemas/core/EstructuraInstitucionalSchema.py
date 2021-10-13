from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import longitud_maxima
from datetime import date


class EstructuraInstitucionalSchema(BaseModel):
    id: int
    documento_aprobacion: str
    fecha_aprobacion: date


class EstructuraInstitucionalPostSchema(BaseModel):
    documento_aprobacion: str = Field(...)
    fecha_aprobacion: date = Field(...)

    @validator('documento_aprobacion')
    def documento_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 8)
        if r:
            return value

    @validator('fecha_aprobacion')
    def fecha_aprobacion_validaciones(cls, value):
        today = date.today()
        if value > today:
            raise ValueError(
                'La fecha de aprobación no debe ser mayor a la fecha actual')
        return value

    class Config:
        schema_extra = {
            "example": {
                "documento_aprobacion": "RESOLUCION No. 024-01-2020",
                "fecha_aprobacion": date(2020, 9, 30)

            }
        }


class EstructuraInstitucionalPutSchema(BaseModel):
    id: int
    documento_aprobacion: str = Field(...)
    fecha_aprobacion: date = Field(...)

    @validator('documento_aprobacion')
    def documento_aprobacion_validaciones(cls, value):
        r = longitud_maxima(80, value, 8)
        if r:
            return value

    @validator('fecha_aprobacion')
    def fecha_aprobacion_validaciones(cls, value):
        today = date.today()
        if value > today:
            raise ValueError(
                'La fecha de aprobación no debe ser mayor a la fecha actual')
        return value
