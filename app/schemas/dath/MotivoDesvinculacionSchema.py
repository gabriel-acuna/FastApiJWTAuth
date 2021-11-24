from pydantic import BaseModel, Field


class MotivoDesvinculacionSchema(BaseModel):
    id: str
    motivo: str


class MotivoDesvinculacionPostSchema(BaseModel):
    motivo: str = Field(...)


class MotivoDesvinculacionPutSchema(BaseModel):
    id: str = Field(...)
    motivo: str = Field(...)
