from typing import Dict, Optional
from pydantic import BaseModel, Field
import enum
from app.schemas.dath.EstadoSumarioSchema import EstadoSumarioSchema
from app.schemas.dath.RegimenLaboralSchema import RegimenLaboralSchema
from app.schemas.dath.ModalidadContractualSchema import ModalidadContractualSchema
from app.schemas.dath.SancionSchema import SancionSchema

class TipoFalta(str, enum.Enum):
    LEVES = 'LEVES'
    GRAVES = 'GRAVES'


class MES(str, enum.Enum):
    ENERO = 'ENERO '
    FEBREO = 'FEBRERO'
    MARZO = 'MARZO'
    ABRIL = 'ABRIL'
    MAYO = 'MAYO'
    JUNIO = 'JUNIO'
    JULIO = 'JULIO'
    AGOSTO = 'AGOSTO'
    SEPTIEMBRE = 'SEPTIEMBRE'
    OCTUBRE = 'OCTUBRE'
    NOVIEMBRE = 'NOVIEMBRE'
    DICIEMBRE = 'DICIEMBRE'


class RegimenDisciplinarioSchema(BaseModel):
    id: str
    anio_sancion:int
    mes_sancion:MES
    persona: dict
    regimen_laboral: RegimenLaboralSchema
    modalidad_laboral: ModalidadContractualSchema
    tipo_falta: TipoFalta
    sancion = SancionSchema
    aplica_sumario:str
    estado_sumario: EstadoSumarioSchema
    numero_sentencia: Optional[str]


class RegimenDisciplinarioSancionPostSchema(BaseModel):
    sancion: str = Field(...)


class RegimenDisciplinarioSancionPutSchema(BaseModel):
    id: str = Field(...)
    sancion: str = Field(...)
