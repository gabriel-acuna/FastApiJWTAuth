from typing import Optional
from pydantic import BaseModel

import enum

from pydantic.networks import EmailStr
class TipoReferencia(str, enum.Enum):
    PERSONAL = "PERSONAL"
    LABORAL  = "LABORAL"

class ReferenciaSchema(BaseModel):
    id: str
    id_persona: str
    referencia: TipoReferencia
    apellidos: str
    nombres: str
    direccion: str
    correo_electronico: Optional[EmailStr]
    telefono_domicilio: Optional[str]
    telefono_movil: str


class ReferenciaPostSchema(BaseModel):
    id_persona: str
    referencia: TipoReferencia
    apellidos: str
    nombres: str
    direccion: str
    correo_electronico: Optional[EmailStr]
    telefono_domicilio: Optional[str]
    telefono_movil: str

class ReferenciaPutSchema(BaseModel):
    referencia: TipoReferencia
    apellidos: str
    nombres: str
    direccion: str
    correo_electronico: Optional[EmailStr]
    telefono_domicilio: Optional[str]
    telefono_movil: str
    
    
