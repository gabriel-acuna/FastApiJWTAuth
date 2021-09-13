from typing import List
from app.schemas.core.AreaIntitucionalSchema import AreaInstitucionSchema
from app.schemas.core.EstructuraInstitucionalSchema import EstructuraInstitucionalSchema
from pydantic import BaseModel, validator, Field
from app.schemas.validaciones import longitud_maxima

class AreaOrganigrama(BaseModel):
    id_estructura: int
    area :  AreaInstitucionSchema
    areas: List[AreaInstitucionSchema]

class OrganigramaSchema(BaseModel):
    estructura: EstructuraInstitucionalSchema
    oraganigrama:List[AreaOrganigrama]


class OrganigramaPostSchema(BaseModel):
    id_estructura: int = Field(...)
    id_area:int
    areas: List[int]
    