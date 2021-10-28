from pydantic import BaseModel, Field

class TipoBecaSchema(BaseModel):
    id:str
    tipo_beca: str

class TipoBecaPostSchema(BaseModel):
    tipo_beca:str = Field(...)

class TipoBecaPutSchema(BaseModel):
    id:str = Field(...)
    tipo_beca: str = Field(...)