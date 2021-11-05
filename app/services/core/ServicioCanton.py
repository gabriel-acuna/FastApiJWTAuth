import logging
from app.schemas.core.CantonSchema import *

from typing import List
from app.models.core.modelos_principales import Canton


class ServicioCanton():

    @classmethod
    async def listar(cls) -> List[CantonSchema]:
        cantones: List[CantonSchema] = []
        try:
            filas = await Canton.listar()
            for fila in filas:
                cantones.append(CantonSchema(**fila[0].__dict__))

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return cantones

    @classmethod
    async def buscar_por_id(cls, id: int) -> CantonSchema:
        canton: CantonSchema = None
        try:
            respuesta = await Canton.obtener(id)
            if respuesta:
                canton = CantonSchema(id=respuesta[0].id,
                                      provincia_id=respuesta[0].provincia_id,
                                      canton=respuesta[0].canton
                                      )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return canton

    @classmethod
    async def agregar_registro(cls, canton: CantonPostSchema):
        try:
            return await Canton.crear(
                canton=canton.canton,
                provincia_id=canton.provincia_id
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, canton: CantonPutSchema):
        try:
            return await Canton.actualizar(
                id=canton.id,
                canton=canton.canton,
                provincia_id=canton.provincia_id
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: int):
        try:
            return await Canton.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, canton: CantonPostSchema) -> bool:
        try:
            existe = await Canton.filtarPor(canton=canton.canton)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
