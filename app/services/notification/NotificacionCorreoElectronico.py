from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from decouple import config as cfg
from fastapi import BackgroundTasks
 

class NotificationCorreoElectronico:

    conf = ConnectionConfig(
        MAIL_USERNAME=cfg('MAIL_USERNAME'),
        MAIL_PASSWORD=cfg('MAIL_PASSWORD'),
        MAIL_FROM=cfg('MAIL_FROM'),
        MAIL_PORT=cfg('MAIL_PORT'),
        MAIL_SERVER=cfg('MAIL_SERVER'),
        MAIL_FROM_NAME=cfg('MAIL_FROM_NAME'),
        MAIL_TLS=True,
        MAIL_SSL=False,
        USE_CREDENTIALS=True,
        TEMPLATE_FOLDER='./templates/email'
    )

    @classmethod
    async def enviar_correo_asinconico(cls,subject: str, email_to: str, body: dict):
        message = MessageSchema(
            subject=subject,
            recipients=[email_to],
            body=body,
            subtype='html',
        )

        fm = FastMail(cls.conf)

        await fm.send_message(message, template_name='email.html')

    @classmethod
    def enviar_correo_en_segundo_plano(cls,background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict):
        message = MessageSchema(
            subject=subject,
            recipients=[email_to],
            body=body,
            subtype='html',
        )

        fm = FastMail(cls.conf)

        background_tasks.add_task(
            fm.send_message, message, template_name='email.html')
