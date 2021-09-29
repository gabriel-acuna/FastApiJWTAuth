from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.core.ProvinciaSchema import ProvinciaSchema
from app.schemas.core.CantonSchema import CantonSchema


class DireccionSchema(BaseModel):
    id: str
    provincia: ProvinciaSchema
    canton: CantonSchema
    parroquia: str
    calle1: str
    calle2: Optional[str]
    referencia: Optional[str]


class DireccionPostSchema(BaseModel):
    id_provincia: int = Field(...)
    id_canton: int = Field(...)
    parroquia: str = Field(...)
    calle1: str = Field(...)
    calle2: Optional[str] = Field()
    referencia: Optional[str] = Field()


class DireccionPutSchema(BaseModel):
    id_provincia: int = Field(...)
    id_canton: int = Field(...)
    parroquia: str = Field(...)
    calle1: str = Field(...)
    calle2: Optional[str] = Field()
    referencia: Optional[str] = Field()
