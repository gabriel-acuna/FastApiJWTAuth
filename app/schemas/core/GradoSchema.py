from pydantic import BaseModel, Field

class GradoSchema(BaseModel):
    id:str
    grado: str

class GradoPostSchema(BaseModel):
    grado:str = Field(...)

class GradoPutSchema(BaseModel):
    id:str = Field(...)
    grado: str = Field(...)