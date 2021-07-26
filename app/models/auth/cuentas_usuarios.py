from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from app.models import Base
from sqlalchemy import Column, String, 
from sqlalchemy.dialects.postgresql import UUID

""" 
    Autor: Ing. Gabriel Acuña
    Descripción: Este módulo contiene los modelos encargados de la gestión de cuentas de usuario y roles
"""

rol_usuario = Table(
    'roles_usuarios',
    Base.metadata,
    Column('rol_id', ForeignKey('roles.id')),
    Column('right_id', ForeignKey('cuentas_usuarios.id'))

)


class Rol(Base):
    __tablename__ = "roles"
    id = Column(UUID, primary_key=True, index=True)
    rol = Column(String(50),)
    descripcion = Column(String(120),)
    usuario = relationship("CuentaUsuario", secondary = rol_usuario)

class CuentaUsuario(Base):
    __tablename__ = "cuentas_usuarios"
    id = Column(UUID, primary_key=True, index=True)
    primer_nombre = Column(String(30),)
    segundo_nombre = Column(String(30),)
    primer_apellido = Column(String(30),)
    segundo_segundo = Column(String(30),)
    email = Column(String,)
    clave_encriptada = column(String(),)
