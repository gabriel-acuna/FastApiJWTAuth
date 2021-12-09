from pydantic import BaseModel, Field
from datetime import date


class EvaluacionPersonalSchema(BaseModel):
    id: str
    id_persona: str
    desde: date
    hasta: date
    puntaje: float
    calificacion: str


class EvaluacionPersonalPostSchema(BaseModel):
    id_persona: str = Field(...)
    desde: date = Field(...)
    hasta: date = Field(...)
    puntaje: float = Field(...)
    calificacion: str = Field(...)


class EvaluacionPersonalPostSchema(BaseModel):
    id_persona: str = Field(...)
    desde: date = Field(...)
    hasta: date = Field(...)
    puntaje: float = Field(...)
    calificacion: str = Field(...)
