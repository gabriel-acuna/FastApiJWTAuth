from pydantic import BaseModel, Field
from app.schemas.core.ProvinciaSchema import ProvinciaSchema
from app.schemas.core.CantonSchema import CantonSchema


class DireccionSchema(BaseModel):
    id: str
    provincia: ProvinciaSchema
    canton: CantonSchema
    parroquia: str
    calle1: str
    calle2: str
    referencia: str


class DireccionPostSchema(BaseModel):
    id_provincia: int = Field(...)
    id_canton: int = Field(...)
    calle1: str = Field(...)
    calle2: str = Field()
    referencia: str = Field(...)


class DireccionPutSchema(BaseModel):
    id_provincia: int = Field(...)
    id_canton: int = Field(...)
    calle1: str = Field(...)
    calle2: str = Field()
    referencia: str = Field(...)
