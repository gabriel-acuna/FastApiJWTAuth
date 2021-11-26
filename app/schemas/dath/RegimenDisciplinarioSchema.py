from typing import Dict, Optional
from pydantic import BaseModel, Field
import enum
from app.schemas.dath.EstadoSumarioSchema import EstadoSumarioSchema
from app.schemas.dath.InformacionPersonalSchema import InformacionPersonalBasicaSchema
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
    persona: InformacionPersonalBasicaSchema
    regimen_laboral: RegimenLaboralSchema
    modalidad_contractual: ModalidadContractualSchema
    tipo_falta: TipoFalta
    sancion = SancionSchema
    aplica_sumario:str
    estado_sumario: EstadoSumarioSchema
    numero_sentencia: Optional[str]


class RegimenDisciplinarioPostSchema(BaseModel):
    anio_sancion:int = Field(...)
    mes_sancion:MES = Field(...)
    persona: str = Field(...)
    regimen_laboral: str = Field(...)
    modalidad_contractual: str = Field(...)
    tipo_falta: TipoFalta = Field(...)
    sancion: str = Field(...)
    aplica_sumario:str = Field(...)
    estado_sumario:str = Field(...)
    numero_sentencia: Optional[str] = Field()


class RegimenDisciplinarioPutSchema(BaseModel):
    id: str = Field(...)
    anio_sancion:int = Field(...)
    mes_sancion:MES = Field(...)
    persona: str = Field(...)
    regimen_laboral: str = Field(...)
    modalidad_contractual: str = Field(...)
    tipo_falta: TipoFalta = Field(...)
    sancion: str = Field(...)
    aplica_sumario:str = Field(...)
    estado_sumario:str = Field(...)
    numero_sentencia: Optional[str] = Field()
