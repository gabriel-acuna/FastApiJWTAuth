from pydantic import BaseModel, Field


class SancionSchema(BaseModel):
    id: str
    sancion: str


class SancionPostSchema(BaseModel):
    sancion: str = Field(...)


class SancionPutSchema(BaseModel):
    id: str = Field(...)
    sancion: str = Field(...)
