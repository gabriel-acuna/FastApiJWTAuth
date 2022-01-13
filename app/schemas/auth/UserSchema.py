from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

from app.schemas.auth.RolSchema import RolSchema


class UserSchema(BaseModel):
    id: Optional[str]
    primer_nombre: str
    segundo_nombre: str
    primer_apellido: str
    segundo_apellido: str 
    email_personal: EmailStr
    email_institucional: EmailStr
    estado: Optional[bool]
    roles: Optional[List[RolSchema]]


class UserPostSchema(BaseModel):
    primer_nombre: str = Field(...)
    segundo_nombre: str = Field(...)
    primer_apellido: str = Field(...)
    segundo_apellido: str = Field(...)
    email_personal: EmailStr
    email_institucional: EmailStr
    roles: List[RolSchema]



class UserPutSchema(BaseModel):
    id: str = Field(...)
    roles: List[RolSchema]
    estado: bool = Field(...)


class ChangePasswordSchema(BaseModel):
    email: EmailStr = Field(...)
    clave_actual: str = Field(...)
    clave_nueva: str = Field(...)
