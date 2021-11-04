from datetime import datetime
from pydantic import Field, BaseModel
from app.schemas.validaciones import longitud_maxima


class ProvinciaSchema(BaseModel):
    id: int
    provincia: str


class ProvinciaPostSchema(BaseModel):
    provincia: str = Field(...)


class ProvinciaPutSchema(BaseModel):
    id: int = Field(...)
    provincia: str = Field(...)
