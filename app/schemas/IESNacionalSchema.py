from pydantic import BaseModel, Field

class IESNacionalSchema(BaseModel):
    id: str
    codigo:str
    institucion:str 

class IESNacionalPostSchema(BaseModel):
    codigo:str = Field(...)
    institucion:str = Field(...)


class IESNacionalPutSchema(BaseModel):
    id: str = Field(...)
    codigo:str = Field(...)
    institucion:str = Field( ...)