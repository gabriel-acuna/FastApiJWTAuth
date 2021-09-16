from datetime import datetime
from pydantic import Field, BaseModel
from app.schemas.validaciones import longitud_maxima


class ProvinciaSchema(BaseModel):
    id:int
    provincia:str
