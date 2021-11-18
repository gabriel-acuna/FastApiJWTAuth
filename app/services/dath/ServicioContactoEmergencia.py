from app.models.dath.modelos import ContactoEmergencia
from app.schemas.dath.ContactoEmergenciaSchema import *
import logging

class ServicioContactoEmergencia():

    @classmethod
    async def buscar_por_id_persona(cls, id_persona:str) -> ContactoEmergenciaSchema:
        contacto: ContactoEmergenciaSchema = None
        try:
            respuesta =  await ContactoEmergencia.filtarPor(id_persona=id_persona)
            if respuesta:
                contacto = ContactoEmergenciaSchema(**respuesta[0][0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return contacto