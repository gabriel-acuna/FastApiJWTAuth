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
    async def obtner_roles(str:id):
        pass
        
    
