from typing import List, Optional
from sqlalchemy.sql.expression import select
from app.models.auth.cuentas_usuarios import CuentaUsuario, Rol, TipoToken, rol_usuario
from app.schemas.auth.RolSchema import RolSchema
from app.schemas.auth.UserLoginSchema import UserLoginSchema
from app.schemas.auth.UserSchema import UserSchema
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
    async def obtener_roles(cls, id: str) -> List[str]:
        roles: List[str] = []
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            result = await async_db_session.execute(
                '''SELECT r.rol FROM roles_usuarios ru INNER JOIN roles
                r ON ru.rol_id=r.id WHERE ru.usuario_id = :usuario_id''', {'usuario_id': id})
            filas = result.all()
            for fila in filas:
                roles.append(fila[0])
            return roles
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()

    @classmethod
    async def listar_usuarios(cls) -> List[UserSchema]:
        usuarios: List[UserSchema] = []
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            results = await async_db_session.execute(
                '''select c.id, p.primer_nombre, p.segundo_nombre, p.primer_apellido,
                p.segundo_apellido, p.correo_personal, p.correo_institucional, c.estado from 
                datos_personales p left join cuentas_usuarios c on c.email = p.correo_institucional'''
            )
            filas = results.all()
            for usuario in filas:
                roles: List[RolSchema] = []
                usuario_id: str = None
                if usuario[0] is not None:
                    usuario_id = str(usuario[0])
                    results1 = await async_db_session.execute(
                        '''SELECT r.id, r.rol, r.descripcion FROM roles_usuarios ru INNER JOIN roles r ON ru.rol_id=r.id
                    WHERE ru.usuario_id = :usuario_id''', {"usuario_id": usuario_id})

                    lista = results1.all()

                    for item in lista:
                        roles.append(
                            RolSchema(id=str(item[0]), rol=item[1], descripcion=item[2]))

                usuarios.append(
                    UserSchema(
                        id=usuario_id,
                        primer_nombre=usuario[1],
                        segundo_nombre=usuario[2],
                        primer_apellido=usuario[3],
                        segundo_apellido=usuario[4],
                        email_personal=usuario[5],
                        email_institucional=usuario[6],
                        estado=usuario[7],
                        roles=roles
                    )
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return usuarios
