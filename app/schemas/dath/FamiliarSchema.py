from pydantic import BaseModel, Field
from datetime import date
from app.schemas.dath.InformacionPersonalSchema import Sexo


class FamiliarSchema(BaseModel):
    id: str
    id_persona: str
    parentesco: str
    identificacion: str
    nombres: str
    apellidos: str
    sexo: Sexo
    fecha_nacimiento: date
    edad: dict


class FamiliarPostSchema(BaseModel):
    id_persona: str = Field(...)
    parentesco: str = Field(...)
    identificacion: str = Field(...)
    nombres: str = Field(...)
    apellidos: str = Field(...)
    sexo: Sexo = Field(...)
    fecha_nacimiento: date = Field(...)


class FamiliarPutSchema(BaseModel):
    id: str = Field(...)
    parentesco: str = Field(...)
    identificacion: str = Field(...)
    nombres: str = Field(...)
    apellidos: str = Field(...)
    sexo: Sexo = Field(...)
    fecha_nacimiento: date = Field(...)
