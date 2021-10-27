from pydantic import BaseModel, Field

class CampoEducativoAmplioSchema(BaseModel):
    id:str
    codigo: str
    descripcion: str

class CampoEducativoAmplioPostSchema(BaseModel):
    codigo: str = Field(...)
    descripcion: str = Field(...)

class CampoEducativoAmplioPutSchema(BaseModel):
    id:str = Field(...)
    codigo: str = Field(...)
    descripcion: str = Field(...)

class CampoEducativoEspecificoSchema(BaseModel):
    id:str
    codigo_amplio: str
    descripcion: str
    campo:str

class CampoEducativoEspecificoPostSchema(BaseModel):
    codigo: str = Field(...)
    campo_amplio: str = Field()
    descripcion: str = Field(...)

class CampoEducativoEspecificoPutSchema(BaseModel):
    id:str = Field(...)
    campo_amplio: str = Field()
    codigo: str = Field(...)
    descripcion: str = Field(...)

class CampoEducativoDetalladoSchema(BaseModel):
    id:str
    campo_especifico: str
    descripcion: str
    campo:str

class CampoEducativoDetalladoPostSchema(BaseModel):
    codigo: str = Field(...)
    campo_especifico: str = Field()
    descripcion: str = Field(...)

class CampoEducativoDetalladoPutSchema(BaseModel):
    id:str = Field(...)
    campo_especifico: str = Field(...)
    codigo: str = Field(...)
    descripcion: str = Field(...)