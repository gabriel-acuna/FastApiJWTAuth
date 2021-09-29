import logging
from typing import List
from app.models.core.modelos_principales import Pais
from app.schemas.core.PaisSchema import PaisSchema


class ServicioPais:

    @classmethod
    async def listar(cls) -> List[PaisSchema]:
        paises: List[PaisSchema] = []
        try:
            filas = await Pais.listar()
            for fila in filas:
                pais = PaisSchema(**fila[0].__dict__)
                paises.append(pais)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return paises

    @classmethod
    async def buscar_por_id(cls, id: int):
        try:
            return await Pais.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
