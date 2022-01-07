from starlette.background import BackgroundTasks
from app.services.notification.NotificacionCorreoElectronico import NotificacionCorreoElectronico
import pytest 
@pytest.mark.asyncio
async def test_enviar_corero():
    enviado = await NotificacionCorreoElectronico.enviar_correo_asinconico(
        subject="Creación de cuenta de usuario",
        email_to="gabriel.acuna.reg27@gmail.com",
        body={
            'title':'Creación de cuenta de usuario',
            'name': 'Gabriel Acuña Regalado',
            'content': 'Su cuenta de usuario ha sido creada satisfactoriamente, para acceder al sistema deberá usar las siguientes credenciales.',
            'credentials':{
                'email':'gabriel.acuna@unesum.edu.ec',
                'password': 'qwerty09786'
            },
            'recommendation': 'Se recomienda iniciar sesión y realizar cambio de contraseña.'
        }
    )
    assert enviado