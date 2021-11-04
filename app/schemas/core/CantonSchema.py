from pydantic import BaseModel
from pydantic.fields import Field

class CantonSchema(BaseModel):
    id:int
    canton:str
    provincia_id: int

class CantonPostSchema(BaseModel):
    canton:str = Field(...)
    provincia_id: int = Field(...)

class CantonPutSchema(BaseModel):
    id:int = Field(...)
    canton:str = Field(...)
    provincia_id: int = Field(...)