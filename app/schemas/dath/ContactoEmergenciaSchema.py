from typing import Optional
from pydantic import BaseModel
from pydantic.fields import Field

class ContactoEmergenciaSchema(BaseModel):
    id:str
    id_persona:str
    apellidos:str
    nombres: str
    direccion: str
    telefono_domicilio: Optional[str]
    telefono_movil: str

class ContactoEmergenciaPostSchema(BaseModel):
    id_persona:str = Field(...)
    apellidos:str = Field(...)
    nombres: str = Field(...)
    direccion: str = Field(...)
    telefono_domicilio: Optional[str] = Field()
    telefono_movil: str = Field(...)

class ContactoEmergenciaPutSchema(BaseModel):
    id:str = Field(...)
    apellidos:str = Field(...)
    nombres: str = Field(...)
    direccion: str = Field(...)
    telefono_domicilio: Optional[str] = Field()
    telefono_movil: str = Field(...)