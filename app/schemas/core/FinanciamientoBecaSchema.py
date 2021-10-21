from pydantic import BaseModel, Field

class FinanciamientoBecaSchema(BaseModel):
    id:str
    financiamiento: str

class FinanciamientoBecaPostSchema(BaseModel):
    financiamiento:str = Field(...)

class FinanciamientoBecaPutSchema(BaseModel):
    id:str = Field(...)
    financiamiento: str = Field(...)