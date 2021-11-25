from typing import List
from app.schemas.dath.SancionSchema import *
from app.models.dath.modelos import Sancion
import logging


class ServicioSancion():

    @classmethod
    async def listar(cls) -> List[SancionSchema]:
        sanciones: List[SancionSchema] = []
        try:
            filas = await Sancion.listar()
            for fila in filas:
                sanciones.append(**fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return sanciones

    @classmethod
    async def buscar_por_id(cls, id: str) -> SancionSchema:
        sancion: SancionSchema = None
        try:
            respuesta = await Sancion.obtener(id)
            if respuesta:
                sancion = SancionSchema(respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return sancion

    @classmethod
    async def agregar_registro(cls, sancion: SancionPostSchema) -> bool:
        try:
            return await Sancion.crear(
                sancion=sancion.sancion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, sancion: SancionPutSchema):
        try:
            return await Sancion.actualizar(
                id=sancion.id,
                sancion=sancion.sancion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await Sancion.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, sancion: SancionPostSchema) -> bool:
        try:
            existe = await Sancion.filtarPor(sancion=sancion.sancion)
            return True if existe else False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
