from pydantic import BaseModel, Field

class TipoEventoSchema(BaseModel):
    id: str
    evento: str

class TipoEventoPostSchema(BaseModel):
    evento: str = Field(...)

class TipoEventoPutSchema(BaseModel):
    id: str = Field(...)
    evento: str = Field(...)