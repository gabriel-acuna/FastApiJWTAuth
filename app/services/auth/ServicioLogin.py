from typing import Optional
from sqlalchemy.sql.expression import select
from app.models.auth.cuentas_usuarios import CuentaUsuario, Rol, TipoToken, rol_usuario
from app.schemas.auth.UserLoginSchema import UserLoginSchema
import bcrypt
from app.database.conf import async_db_session


class ServicioLogin():

    @classmethod
    async def verificar_usuario(cls, credenciales: UserLoginSchema) -> Optional[CuentaUsuario]:
        usuario: CuentaUsuario = None
        print(credenciales.email)
        resp = await CuentaUsuario.filtarPor(email=credenciales.email)

        if resp:
            usuario = resp[0][0]
        return usuario

    @classmethod
    async def verificar_clave(cls, clave: str, clave_encriptada: str) -> bool:
        return bcrypt.checkpw(b'{clave}', b'{clave_encriptada}')

    @classmethod
    async def obtener_roles(cls, id:str):
        roles = []
        await async_db_session.init()
        result = await async_db_session.execute(
            '''SELECT r.rol FROM roles_usuarios ru INNER JOIN roles
             r ON ru.rol_id=r.id WHERE ru.usuario_id = :usuario_id''', {'usuario_id': id} )
        for fila in result:
            roles.append(fila[0])
        return roles
