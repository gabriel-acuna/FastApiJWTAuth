from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import es_no_numerico, longitud_maxima


class EstadoCivilSchema(BaseModel):
    id: int
    estado_civil: str


class EstadoCivilPostSchema(BaseModel):
    estado_civil:str = Field(...)

    @validator('estado_civil')
    def estado_civil_maxima(cls, value):
        r = longitud_maxima(30, value, 7)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "estado_civil": "SOLTERO/A"
            }
        }


class EstadoCivilPutSchema(BaseModel):
    id: int
    estado_civil:str = Field(...)

    @validator('estado_civil')
    def estado_civil_maxima(cls, value):
        r = longitud_maxima(30, value, 7)
        if r and es_no_numerico(value):
            return value
