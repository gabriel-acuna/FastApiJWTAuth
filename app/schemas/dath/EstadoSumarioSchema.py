from pydantic import BaseModel, Field


class EstadoSumarioSchema(BaseModel):
    id: str
    estado: str


class EstadoSumarioPostSchema(BaseModel):
    estado: str = Field(...)


class EstadoSumarioPutSchema(BaseModel):
    id: str = Field(...)
    estado: str = Field(...)
