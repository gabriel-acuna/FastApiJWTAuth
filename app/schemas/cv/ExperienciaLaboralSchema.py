from typing import Optional
from pydantic import BaseModel, Field
from datetime import date

class ExperienciaLaboralSchema(BaseModel):
    id: str
    id_persona: str
    empresa: str
    lugar: str
    cargo: str
    inicio: date
    fin: Optional[date]

class ExperienciaLaboralPostSchema(BaseModel):
    id_persona: str = Field(...)
    empresa: str = Field(...)
    lugar: str = Field(...)
    cargo: str = Field(...)
    inicio: date = Field(...)
    fin: Optional[date] = Field()

class ExperienciaLaboralPostSchema(BaseModel):
    id: str = Field(...)
    empresa: str = Field(...)
    lugar: str = Field(...)
    cargo: str = Field(...)
    inicio: date = Field(...)
    fin: Optional[date] = Field()

