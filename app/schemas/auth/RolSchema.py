import abc
from pydantic import BaseModel

class RolSchema(BaseModel):
    id: str
    rol: str
    descripcion: str
