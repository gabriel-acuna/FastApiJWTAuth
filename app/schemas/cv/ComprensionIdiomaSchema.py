from pydantic import BaseModel, Field
import enum

class NivelCompresion(str, enum.Enum):
    Excelente = 'Excelente'
    Buena = 'Buena'
    Limitada = 'Limitada'
    Ninguna = 'Ninguna'

class ComprensionIdiomaSchema(BaseModel):
    id: str
    id_persona: str
    idioma: str
    lugar_estudio: str
    nivel_compresion: NivelCompresion

class ComprensionIdiomaPostSchema(BaseModel):
    id_persona: str = Field(...)
    idioma: str = Field(...)
    lugar_estudio: str = Field(...)
    nivel_compresion: NivelCompresion = Field(...)

class ComprensionIdiomaPutSchema(BaseModel):
    id: str = Field(...)
    idioma: str = Field(...)
    lugar_estudio: str = Field(...)
    nivel_compresion: NivelCompresion = Field(...)