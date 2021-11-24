from pydantic import BaseModel, Field

class TipoNombramientoSchema(BaseModel):
    id: str
    nombramiento: str


class TipoNombramientoPostSchema(BaseModel):
    nombramiento: str = Field(...)

class TipoNombramientoPutSchema(BaseModel):
    id: str = Field(...)
    nombramiento: str = Field(...)