from pydantic import BaseModel, Field
import enum

class NivelComprension(str, enum.Enum):
    Excelente = 'Excelente'
    Buena = 'Buena'
    Limitada = 'Limitada'
    Ninguna = 'Ninguna'

class ComprensionIdiomaSchema(BaseModel):
    id: str
    id_persona: str
    idioma: str
    lugar_estudio: str
    nivel_comprension: NivelComprension

class ComprensionIdiomaPostSchema(BaseModel):
    id_persona: str = Field(...)
    idioma: str = Field(...)
    lugar_estudio: str = Field(...)
    nivel_comprension: NivelComprension = Field(...)

class ComprensionIdiomaPutSchema(BaseModel):
    id: str = Field(...)
    idioma: str = Field(...)
    lugar_estudio: str = Field(...)
    nivel_comprension: NivelComprension = Field(...)