from app.models.cv.modelos import TipoEvento
from app.schemas.cv.TipoEventoSchema import *
import logging

from typing import List

class ServicioTipoEvento():

    @classmethod
    async def listar(cls) -> List[TipoEventoSchema]:
        tipo_eventos: List[TipoEventoSchema] = []

        try:
            filas = await TipoEvento.listar()
            for fila in filas:
                tipo_eventos.append(TipoEventoSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return tipo_eventos

    @classmethod
    async def buscar_por_id(cls, id: str) -> TipoEventoSchema:
        tipo_evento: TipoEventoSchema = None

        try:
            respuesta = await TipoEvento.obtener(id)
            if respuesta:
                tipo_evento = TipoEventoSchema(
                    **respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return tipo_evento

    @classmethod
    async def agregar_registro(cls,  tipo_evento: TipoEventoPostSchema):

        try:
            return await TipoEvento.crear(
                evento = tipo_evento.evento
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, tipo_evento: TipoEventoPutSchema):
        try:
            return await TipoEvento.actualizar(
                id=tipo_evento.id,
                evento = tipo_evento.evento
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await TipoEvento.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, tipo_evento: TipoEventoPostSchema) -> bool:
        try:
            existe = await TipoEvento.filtarPor(evento = tipo_evento.evento)
            if existe:
                return True
            return False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
