from datetime import date
from typing import Optional
from pydantic import BaseModel
import enum
from app.schemas.core.TipoDocumentoSchema import TipoDocumentoSchema
from app.schemas.core.RelacionIESSchema import RelacionIESSchema
from app.schemas.core.TipoEscalafonNombramientoSchema import TipoEscalafonNombramientoSchema
from app.schemas.core.CategoriaContratoProfesorSchema import CategoriaContratoProfesorSchema
from app.schemas.core.TiempoDedicacionProfesorSchema import TiempoDedicacionProfesorSchema
from app.schemas.core.TipoFuncionarioSchema import TipoFuncionarioSchema
from app.schemas.core.AreaInstitucionalSchema import AreaInstitucionSchema
from app.schemas.core.TipoDocenteLOESSchema import TipoDocenteLOESSchema
from app.schemas.core.CategoriaDocenteLOSEPSchema import CategoriaDocenteLOSEPSchema
from app.schemas.core.NivelEducativoSchema import NivelEducativoSchema

class TipoPersonal(str, enum.Enum):
    FUNCIONARIIO = "FUNCIONARIO"
    PROFESOR = "PROFESOR"

class Opciones(str, enum.Enum):
    SI = "SI"
    NO = "NO"

class DetalleExpedienteSchema(BaseModel):
    id:str
    id_expediente:str
    tipo_personal: TipoPersonal
    tipo_documento: TipoDocumentoSchema
    motivo_accion: Optional[str]
    numero_documento: str
    contrato_relacionado: Optional[str]
    ingreso_concurso: Opciones
    relacion_ies: RelacionIESSchema
    escalafon_nombramiento: Optional[TipoEscalafonNombramientoSchema]
    categoria_contrato: Optional[CategoriaContratoProfesorSchema]
    tiempo_dedicacion:Optional[TiempoDedicacionProfesorSchema]
    remuneracion_mensual: float
    remuneracion_hora: Optional[float]
    fecha_inicio: date
    fecha_fin: Optional[date]
    tipo_funcionario: Optional[TipoFuncionarioSchema]
    cargo: Optional[str]
    tipo_docente: Optional[TipoDocenteLOESSchema]
    categoria_docente = Optional[CategoriaDocenteLOSEPSchema]
    puesto_jerarquico = Optional[Opciones]
    horas_laborables_semanales = Optional[int]
    area: AreaInstitucionSchema
    sub_area: Optional[AreaInstitucionSchema]
    nivel: NivelEducativoSchema


