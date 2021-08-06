from app.schemas.core.CantonSchema import CantonSchema

from typing import List
from app.models.core.modelos_principales import Canton


class ServicioCanton():
    __canton: Canton = Canton()

    @classmethod
    async def listar(cls) -> List[CantonSchema]:
        cantones: List[CantonSchema] = []
        try:
            filas = await cls.__canton.listar()
            for fila in filas:
                cantones.append(CantonSchema(**fila[0].__dict__))

        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
        return cantones

    @classmethod
    async def buscar_por_id(cls, id: int):
        try:
            return await cls.__canton.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
