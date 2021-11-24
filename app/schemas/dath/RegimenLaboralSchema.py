
from pydantic import BaseModel, Field


class RegimenLaboralSchema(BaseModel):
    id: str
    regimen: str


class RegimenLaboralPostSchema(BaseModel):
    regimen: str = Field(...)


class RegimenLaboralPostSchema(BaseModel):
    id: str = Field(...)
    regimen: str = Field(...)
