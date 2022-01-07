from pathlib import Path
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from decouple import config as cfg
from fastapi import BackgroundTasks
import logging


class NotificacionCorreoElectronico():

    __conf = ConnectionConfig(
        MAIL_USERNAME=cfg('MAIL_USERNAME'),
        MAIL_PASSWORD=cfg('MAIL_PASSWORD'),
        MAIL_FROM=cfg('MAIL_FROM'),
        MAIL_PORT=cfg('MAIL_PORT'),
        MAIL_SERVER=cfg('MAIL_SERVER'),
        MAIL_FROM_NAME=cfg('MAIL_FROM_NAME'),
        MAIL_TLS=True,
        MAIL_SSL=False,
        USE_CREDENTIALS=True,
        TEMPLATE_FOLDER=Path(__file__).parent / 'templates/email',
        VALIDATE_CERTS=False
    )

    @classmethod
    async def enviar_correo_asinconico(cls, subject: str, email_to: str, body: dict) -> bool:
        try:
            message = MessageSchema(
                subject=subject,
                recipients=[email_to],
                template_body=body,
                subtype='html',
            )

            fm = FastMail(cls.__conf)

            await fm.send_message(message, template_name='email.html')
            return True
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
            return False

    @classmethod
    def enviar_correo_en_segundo_plano(cls, background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict) -> bool:
        try:
            message = MessageSchema(
                subject=subject,
                recipients=[email_to],
                body=body,
                subtype='html',
            )

            fm = FastMail(cls.__conf)

            background_tasks.add_task(
                fm.send_message, message, template_name='email.html')
            return True
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
            return False
