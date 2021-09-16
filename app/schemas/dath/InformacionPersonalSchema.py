from pydantic.networks import EmailStr
from app.schemas.core.EstadoCivilSchema import EstadoCivilSchema
from datetime import date
from app.models.dath.modelos import DireccionDomicilio, TipoPersonal
from app.schemas.core.PaisSchema import PaisPutSchema
from pydantic import BaseModel, Field
from app.schemas.dath.DireccionSchema import *
from app.schemas.core.DiscapacidadSchema import DiscapacidadSchema
from app.schemas.core.EtniaSchema import EtniaSchema
from app.schemas.core.NacionalidadSchema import NacionalidadSchema
import enum


class TipoIdentificacion(str, enum.Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"


class Sexo(str, enum.Enum):
    HOMBRE = "HOMBRE"
    MUJER = "MUJER"


class InformacionPersonalSchema(BaseModel):
    tipo_identificacion: TipoIdentificacion
    identificacion: str
    primer_nombre: str
    segundo_nombre: str
    primer_apellido: str
    segundo_apellido: str
    sexo: Sexo
    fecha_nacimiento: date
    edad: dict
    pais_origen: PaisPutSchema
    estado_civil: EstadoCivilSchema
    discapacidad: DiscapacidadSchema
    carnet_conadis: str
    porcentaje_discapacidad: int
    etnia: EtniaSchema
    nacionalidad: NacionalidadSchema
    correo_institucional: EmailStr
    correo_personal: EmailStr
    telefono_domicilio: str
    telefono_movil: str
    direccion_domicilio: DireccionSchema
    tipo_sangre: str
    licencia_conduccion: str


class InformacionPersonalPostSchema(BaseModel):
    tipo_identificacion: TipoIdentificacion
    identificacion: str = Field(...)
    primer_nombre: str = Field(...)
    segundo_nombre: str = Field(...)
    primer_apellido: str = Field(...)
    segundo_apellido: str = Field(...)
    sexo: Sexo
    fecha_nacimiento: date = Field(...)
    pais_origen: int = Field(...)
    estado_civil: int = Field(...)
    discapacidad: int = Field(...)
    carnet_conadis: str = Field()
    porcentaje_discapacidad: int = Field(...)
    etnia: int = Field(...)
    nacionalidad: int = Field(...)
    correo_institucional: EmailStr = Field(...)
    correo_personal: EmailStr = Field(...)
    telefono_domicilio: str = Field(...)
    telefono_movil: str = Field(...)
    direccion_domicilio: DireccionPostSchema
    tipo_sangre: str = Field(...)
    licencia_conduccion: str = Field()


class InformacionPersonalPutSchema(BaseModel):
    tipo_identificacion: TipoIdentificacion
    primer_nombre: str
    segundo_nombre: str
    primer_apellido: str
    segundo_apellido: str
    sexo: Sexo
    fecha_nacimiento: date
    edad: dict
    pais_origen: int
    estado_civil: int
    discapacidad: int
    carnet_conadis: str
    porcentaje_discapacidad: int
    etnia: int
    nacionalidad: int
    correo_institucional: EmailStr
    correo_personal: EmailStr
    telefono_domicilio: str
    telefono_movil: str
    direccion_domicilio: DireccionPutSchema
    tipo_sangre: str
    licencia_conduccion: str
