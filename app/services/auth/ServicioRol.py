from typing import List
from app.models.auth.cuentas_usuarios import Rol
from app.schemas.auth.RolSchema import *
import logging


class ServicioRol():

    @classmethod
    async def listar(cls) -> List[RolSchema]:
        roles: List[RolSchema] = []
        try:
            filas = await Rol.listar()
            for fila in filas:
                roles.append(
                    RolSchema(**fila[0].__dict__)
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return roles

    @classmethod
    async def buscar_por_id(cls, id: str) -> RolSchema:
        rol: RolSchema = None
        try:
            resultado = await Rol.obtener(id)
            if resultado:
                rol = RolSchema(**resultado[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return rol


    @classmethod
    async def agregar_registro(cls, rol: RolPostSchema) -> bool:
        try:
            return await Rol.crear(
                rol = rol.rol,
                descripcion = rol.descripcion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, rol: RolPutSchema) -> bool:
        try:
            return await Rol.actualizar(
                id = rol.id,
                rol = rol.rol,
                descripcion = rol.descripcion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await Rol.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, rol: RolPostSchema) -> bool:
        try:
            existe = await Rol.filtarPor(rol = rol.rol)
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

