from pydantic import BaseModel


class InfoIESSchema(BaseModel):
    ies: str
    codigo_ies: int
    provincia: str
    canton: str
    url: str
    documentacion_api: str
