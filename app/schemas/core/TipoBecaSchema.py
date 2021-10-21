from pydantic import BaseModel, Field

class TipoBecaSchema(BaseModel):
    id:str
    tipoBeca: str

class TipoBecaPostSchema(BaseModel):
    tipoBeca:str = Field(...)

class TipoBecaPutSchema(BaseModel):
    id:str = Field(...)
    tipoBeca: str = Field(...)