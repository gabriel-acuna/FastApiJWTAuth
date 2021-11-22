from pydantic import BaseModel, Field
import enum


class TipoCuenta(str, enum.Enum):
    AHORRO = "AHORRO"
    CORRIENTE = "CORRIENTE"


class InformacionBancariaSchema(BaseModel):
    id: str
    institucion_financiera: str
    tipo_cuenta: TipoCuenta
    numero_cuenta: str

class InformacionBancariaPostSchema(BaseModel):
    institucion_financiera: str = Field(...)
    tipo_cuenta: TipoCuenta = Field(...)
    numero_cuenta: str = Field(...)