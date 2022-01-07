from typing import Optional
from pydantic import BaseModel, Field


class RolSchema(BaseModel):
    id: str
    rol: str
    descripcion: Optional[str]


class RolPostSchema(BaseModel):
    rol: str = Field(...)
    descripcion: Optional[str] = Field()

class RolPutSchema(BaseModel):
    id: str = Field(...)
    rol: str = Field(...)
    descripcion: Optional[str] = Field()