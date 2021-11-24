from pydantic import BaseModel, Field


class TipoContratoSchema(BaseModel):
    id: str
    contrato: str


class TipoContratoPostSchema(BaseModel):
    contrato: str = Field(...)


class TipoContratoPostSchema(BaseModel):
    id: str = Field(...)
    contrato: str = Field(...)
