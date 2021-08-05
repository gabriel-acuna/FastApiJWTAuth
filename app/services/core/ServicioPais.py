from typing import List
from app.models.core.modelos_principales import Pais
from app.schemas.core.PaisSchema import PaisSchema
class ServicioPais:
    __pais: Pais =Pais()

    @classmethod
    async def listar(cls) -> List[PaisSchema]:
        paises: List[PaisSchema] = []
        filas = await cls.__pais.listar()
        for fila in filas:
            paises.append(PaisSchema(**fila[0].__dict__))
        return paises
    

    @classmethod
    async def buscar_por_id(cls, id:int):
        return await cls.__pais.obtener(id)