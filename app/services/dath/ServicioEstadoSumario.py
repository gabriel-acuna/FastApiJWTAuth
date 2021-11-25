from typing import List
from app.schemas.dath.EstadoSumarioSchema import *
from app.models.dath.modelos import EstadoSumario
import logging


class ServicioEstadoSumario():

    @classmethod
    async def listar(cls) -> List[EstadoSumarioSchema]:
        estados: List[EstadoSumarioSchema] = []
        try:
            filas = await EstadoSumario.listar()
            for fila in filas:
                estados.append(**fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return estados

    @classmethod
    async def buscar_por_id(cls, id: str) -> EstadoSumarioSchema:
        estado: EstadoSumarioSchema = None
        try:
            respuesta = await EstadoSumario.obtener(id)
            if respuesta:
                estado = EstadoSumarioSchema(respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return estado

    @classmethod
    async def agregar_registro(cls, estado: EstadoSumarioPostSchema) -> bool:
        try:
            return await EstadoSumario.crear(
                estado=estado.estado
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, estado: EstadoSumarioPutSchema):
        try:
            return await EstadoSumario.actualizar(
                id=estado.id,
                estado=estado.estado
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await EstadoSumario.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, estado: EstadoSumarioPostSchema) -> bool:
        try:
            existe = await EstadoSumario.filtarPor(estado=estado.estado)
            return True if existe else False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
