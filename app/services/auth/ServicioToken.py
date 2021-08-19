from app.models.auth.cuentas_usuarios import TokenAutorizacion
from datetime import datetime


class ServicioToken():

    @classmethod
    async def agregar_registro(**kwargs) -> bool:
        try:
            return await TokenAutorizacion.crear(
                tipo_token=kwargs['tipo_token'],
                token=kwargs['token'],
                usuario_id=kwargs['usuario_id']

            )
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(**kwargs) -> bool:
        try:
            token: TokenAutorizacion
            resp = await TokenAutorizacion.filtarPor(token=kwargs['token'])
            if resp:
                token = resp[0][0]
                token.estado = False
                token.usado_hasta = datetime.now(0)
                return await TokenAutorizacion.actualizar(
                    id=token.id, estado=token.estado, usado_hasta=token.usado_hasta)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
