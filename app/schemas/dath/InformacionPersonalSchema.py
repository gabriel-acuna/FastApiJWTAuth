from typing import Optional
from pydantic.networks import EmailStr
from pydantic.utils import T
from app.schemas.core.EstadoCivilSchema import EstadoCivilSchema
from datetime import date
from app.schemas.core.PaisSchema import PaisSchema
from pydantic import BaseModel, Field, validator
from app.schemas.dath.ContactoEmergenciaSchema import *
from app.schemas.dath.DireccionSchema import *
from app.schemas.core.DiscapacidadSchema import DiscapacidadSchema
from app.schemas.core.EtniaSchema import EtniaSchema
from app.schemas.core.NacionalidadSchema import NacionalidadSchema
import enum
from app.schemas.validaciones import longitud_maxima, validar_cedula
from datetime import date


class TipoIdentificacion(str, enum.Enum):
    CEDULA = "CEDULA"
    PASAPORTE = "PASAPORTE"


class Sexo(str, enum.Enum):
    HOMBRE = "HOMBRE"
    MUJER = "MUJER"

class TipoLicenciaConduccion(str,enum.Enum):
    A = 'A'
    A1 = 'A1'
    B = 'B'
    C = 'C'
    C1 = 'C1'
    D = 'D'
    D1 = 'D1'
    E = 'E'
    E1 = 'E1'
    F = 'F'
    G = 'G'

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
    pais_origen: PaisSchema
    estado_civil: EstadoCivilSchema
    discapacidad: DiscapacidadSchema
    carnet_conadis: str
    porcentaje_discapacidad: int
    etnia: EtniaSchema
    nacionalidad: Optional[NacionalidadSchema]
    correo_institucional: EmailStr
    correo_personal: EmailStr
    telefono_domicilio: Optional[str]
    telefono_movil: str
    direccion_domicilio: DireccionSchema
    contacto_emergencia: Optional[ContactoEmergenciaSchema]
    tipo_sangre: str
    licencia_conduccion: str
    tipo_licencia:Optional[TipoLicenciaConduccion]
    fecha_ingreso: date

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
    discapacidad: str = Field(...)
    carnet_conadis: Optional[str]
    porcentaje_discapacidad: int = Field(...)
    etnia: str = Field(...)
    nacionalidad: Optional[str]
    correo_institucional: EmailStr = Field(...)
    correo_personal: EmailStr = Field(...)
    telefono_domicilio: Optional[str]
    telefono_movil: str = Field(...)
    direccion_domicilio: DireccionPostSchema
    contacto_emergencia: ContactoEmergenciaPostSchema
    tipo_sangre: str = Field(...)
    licencia_conduccion: str = Field(...)
    tipo_licencia: Optional[TipoLicenciaConduccion] = Field()
    fecha_ingreso: date
    
    @validator("identificacion")
    def identificacion_validaciones(cls, field_value, values, field, config):
        print( "test",validar_cedula(field_value))
        r =  longitud_maxima(10, field_value)
       
        
        if values['tipo_identificacion'] == TipoIdentificacion.CEDULA and validar_cedula(field_value):
            return field_value
        elif values['tipo_identificacion'] == TipoIdentificacion.PASAPORTE and r:
            return field_value
    
    @validator("fecha_ingreso")
    def fecha_ingreso_validaciones(cls, value):
        hoy = date.today()
        if value > hoy:
            raise ValueError("La fecha de ingreso no puede ser mayor a la fecha actual")
        return value
        




class InformacionPersonalPutSchema(BaseModel):
    tipo_identificacion: TipoIdentificacion
    primer_nombre: str = Field(...)
    segundo_nombre: str = Field(...)
    primer_apellido: str = Field(...)
    segundo_apellido: str = Field(...)
    sexo: Sexo
    fecha_nacimiento: date = Field(...)
    pais_origen: int = Field(...)
    estado_civil: int = Field(...)
    discapacidad: str = Field(...)
    carnet_conadis: Optional[str]
    porcentaje_discapacidad: int = Field(...)
    etnia: str = Field(...)
    nacionalidad: Optional[str]
    correo_institucional: EmailStr = Field(...)
    correo_personal: EmailStr = Field(...)
    telefono_domicilio: Optional[str]
    telefono_movil: str = Field(...)
    direccion_domicilio: DireccionPostSchema
    contacto_emergencia: ContactoEmergenciaPostSchema
    tipo_sangre: str = Field(...)
    licencia_conduccion: str = Field(...)
    tipo_licencia: Optional[TipoLicenciaConduccion] = Field()
    fecha_ingreso:date
    
    @validator("fecha_ingreso")
    def fecha_ingreso_validaciones(cls, value):
        hoy = date.today()
        if value > hoy:
            raise ValueError("La fecha de ingreso no puede ser mayor a la fecha actual")
        return value