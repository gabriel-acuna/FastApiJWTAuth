import logging
from app.schemas.core.CantonSchema import CantonSchema

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
    async def buscar_por_id(cls, id: int):
        try:
            return await Canton.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)