from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import es_no_numerico, longitud_maxima

class EstructuraInstitucionalSchema(BaseModel):
    id: int
    nombre:str
    codigo: str
    id_area: int

class EstructuraInstitucionalPostSchema(BaseModel):
    nombre:str  = Field(...)
    codigo: str
    id_area: int
    
    @validator('nombre')
    def nombre_validaciones(cls, value):
        r = longitud_maxima(30, value, 3)
        if r and es_no_numerico(value):
            return value

    class Config:
        schema_extra = {
            "example": {
                "nombre": "OCS"
            }
        }


class EstructuraInstitucionalPutSchema(BaseModel):
    id: int
    nombre:str = Field(...)
    codigo: str
    id_area:id
