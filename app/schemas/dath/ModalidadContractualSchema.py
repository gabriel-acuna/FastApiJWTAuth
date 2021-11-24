
from pydantic import BaseModel, Field


class ModalidadContractualSchema(BaseModel):
    id: str
    modalidad: str


class ModalidadContractualPostSchema(BaseModel):
    modalidad: str = Field(...)


class ModalidadContractualPutSchema(BaseModel):
    id: str = Field(...)
    modalidad: str = Field(...)
