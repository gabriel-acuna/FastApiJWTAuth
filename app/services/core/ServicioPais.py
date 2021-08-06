from typing import List
from app.models.core.modelos_principales import Pais
from app.schemas.core.PaisSchema import PaisSchema


class ServicioPais:
    __pais: Pais = Pais()

    @classmethod
    async def listar(cls) -> List[PaisSchema]:
        paises: List[PaisSchema] = []
        try:
            filas = await cls.__pais.listar()
            for fila in filas:
                paises.append(PaisSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
        return paises

    @classmethod
    async def buscar_por_id(cls, id: int):
        try:
            return await cls.__pais.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
