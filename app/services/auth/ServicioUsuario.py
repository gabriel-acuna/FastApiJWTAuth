from typing import Optional
from sqlalchemy.sql.expression import select
from app.models.auth.cuentas_usuarios import CuentaUsuario, Rol, TipoToken, rol_usuario
from app.schemas.auth.UserLoginSchema import UserLoginSchema
import bcrypt
from app.database.conf import AsyncDatabaseSession
import logging


class ServicioUsuario():

    @classmethod
    async def verificar_usuario(cls, credenciales: UserLoginSchema) -> Optional[CuentaUsuario]:
        usuario: CuentaUsuario = None
        resp = await CuentaUsuario.filtarPor(email=credenciales.email)

        if resp:
            usuario = resp[0][0]
        return usuario

    @classmethod
    async def verificar_clave(cls, clave: str, clave_encriptada: str) -> bool:
        return bcrypt.checkpw(clave.encode(), clave_encriptada.encode())

    @classmethod
    async def cambiar_clave(cls, id: str, clave: str) -> bool:
        return await CuentaUsuario.actualizar(id=id, clave_encriptada=clave)

    @classmethod
    def cifrar_clave(cls, clave: str) -> str:
        return CuentaUsuario.cifrar_clave(clave)

    @classmethod
    async def obtener_roles(cls, id: str):
        roles = []
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            result = await async_db_session.execute(
                '''SELECT r.rol FROM roles_usuarios ru INNER JOIN roles
                r ON ru.rol_id=r.id WHERE ru.usuario_id = :usuario_id''', {'usuario_id': id})
            for fila in result:
                roles.append(fila[0])
            return roles
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
