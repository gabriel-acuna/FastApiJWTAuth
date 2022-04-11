from typing import List, Optional
from sqlalchemy.sql.expression import select
from app.models.auth.cuentas_usuarios import CuentaUsuario, Rol, TipoToken, rol_usuario
from app.schemas.auth.RolSchema import RolSchema
from app.schemas.auth.UserLoginSchema import UserLoginSchema
from app.schemas.auth.UserSchema import UserPostSchema, UserPutSchema, UserSchema
import bcrypt
from app.utils.generar_clave import generar_calve
from app.database.conf import AsyncDatabaseSession
import logging
from app.services.notification.NotificacionCorreoElectronico import NotificacionCorreoElectronico


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
                '''select c.id, c.primer_nombre, c.segundo_nombre, c.primer_apellido,
                c.segundo_apellido, p.correo_personal, c.email, c.estado from 
                cuentas_usuarios c left join  datos_personales p on c.email = p.correo_institucional'''
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
                        email_personal=usuario[5] if usuario[5] is not None else 'example@mail.com',
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

    @classmethod
    async def buscar_por_id(cls, id: str) -> UserSchema:
        usuario: UserSchema = None
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            results = await async_db_session.execute(
                '''select c.id, c.primer_nombre, c.segundo_nombre, c.primer_apellido,
                c.segundo_apellido, p.correo_personal, c.email, c.estado from 
                cuentas_usuarios c left join  datos_personales p on c.email = p.correo_institucional
                where c.id = :usuario_id''', {"usuario_id": id}
            )
            cuenta_usuario = results.all()
            if cuenta_usuario:
                roles: List[RolSchema] = []
                usuario_id: str = None
                if cuenta_usuario[0][0] is not None:
                    usuario_id = str(cuenta_usuario[0][0])
                    results1 = await async_db_session.execute(
                        '''SELECT r.id, r.rol, r.descripcion FROM roles_usuarios ru INNER JOIN roles r ON ru.rol_id=r.id
                    WHERE ru.usuario_id = :usuario_id''', {"usuario_id": usuario_id})

                    lista = results1.all()

                    for item in lista:
                        roles.append(
                            RolSchema(id=str(item[0]), rol=item[1], descripcion=item[2]))

                usuario = UserSchema(
                    id=usuario_id,
                    primer_nombre=cuenta_usuario[0][1],
                    segundo_nombre=cuenta_usuario[0][2],
                    primer_apellido=cuenta_usuario[0][3],
                    segundo_apellido=cuenta_usuario[0][4],
                    email_personal=cuenta_usuario[0][5] if cuenta_usuario[0][5] is not None else 'example@mail.com',
                    email_institucional=cuenta_usuario[0][6],
                    estado=cuenta_usuario[0][7],
                    roles=roles
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return usuario

    @classmethod
    async def crear_cuenta(cls, usuario: UserPostSchema) -> bool:
        resgistrado: bool = False
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            clave = await generar_calve()
            cuenta_usuario = CuentaUsuario()
            cuenta_usuario.primer_nombre = usuario.primer_nombre
            cuenta_usuario.segundo_nombre = usuario.segundo_nombre
            cuenta_usuario.primer_apellido = usuario.primer_apellido
            cuenta_usuario.segundo_apellido = usuario.segundo_apellido
            cuenta_usuario.email = usuario.email_institucional
            cuenta_usuario.clave_encriptada = cuenta_usuario.cifrar_clave(
                clave)
            async_db_session.add(cuenta_usuario)
            await async_db_session.commit()
            for rol in usuario.roles:
                await async_db_session.execute('''
                INSERT INTO roles_usuarios (usuario_id, rol_id) values  (:usuario_id, :rol_id)
                ''', {"usuario_id": cuenta_usuario.id, "rol_id": rol.id})
            await async_db_session.commit()

            resgistrado = True
            await NotificacionCorreoElectronico.enviar_correo_asinconico(
                subject="Creación de cuenta de usuario",
                email_to=usuario.email_personal,
                body={
                    'title': 'Creación de cuenta de usuario',
                    'name': f'{usuario.primer_nombre} {usuario.segundo_nombre} {usuario.primer_apellido} {usuario.segundo_apellido}',
                    'content': 'Su cuenta de usuario ha sido creada satisfactoriamente, para acceder al sistema deberá usar las siguientes credenciales.',
                    'credentials': {
                        'email': usuario.email_institucional,
                        'password': clave
                    },
                    'recommendation': 'Se recomienda iniciar sesión y realizar cambio de contraseña.'
                }
            )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return resgistrado

    @classmethod
    async def actualizar_cuenta(cls, usuario: UserPutSchema) -> bool:
        actualizado: bool = False
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            await async_db_session.execute('''delete from roles_usuarios where usuario_id = :usuario_id''', {"usuario_id": usuario.id})
            await async_db_session.commit()
            resultado = await async_db_session.execute(select(CuentaUsuario).where(CuentaUsuario.id == usuario.id))
            cuenta_usuario: CuentaUsuario = resultado.scalar_one()
            cuenta_usuario.estado = usuario.estado
            for rol in usuario.roles:
                await async_db_session.execute('''
                INSERT INTO roles_usuarios (usuario_id, rol_id) values  (:usuario_id, :rol_id)
                ''', {"usuario_id": usuario.id, "rol_id": rol.id})
            await async_db_session.commit()
            actualizado = True

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return actualizado
