from datetime import datetime
from pydantic import BaseModel, Field, validator
from app.schemas.validaciones import longitud_maxima


class TipoFuncionarioSchema(BaseModel):
    id: str
    tipo: str
    registrado_en: datetime
    actualizado_en: datetime
    

class TipoFuncionarioPostSchema(BaseModel):
    tipo: str = Field(...)

    @validator("tipo")
    def tipo_funcionario_maxima_longitud(cls, value):
        longitud_maxima(50, value)

    class Config:
        schema_extra = {
            "ejemplo": {
                "tipo": "ADMINISTRATIVO"
            }
        }


class TipoFuncionarioPostSchema(BaseModel):
    id: str = Field(...)
    tipo: str = Field(...)

    @validator("tipo")
    def tipo_funcionario_maxima_longitud(cls, value):
        longitud_maxima(50, value)
