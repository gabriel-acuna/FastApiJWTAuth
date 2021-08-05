from app.schemas.core.CantonSchema import CantonSchema
from typing import List
from app.models.core.modelos_principales import Canton, Provincia
from app.schemas.core.ProvinciaSchema import ProvinciaSchema


class ServicioProvincia():
    __provincia: Provincia = Provincia()
    __canton: Canton = Canton()

    @classmethod
    async def listar(cls) -> List[ProvinciaSchema]:
        provincias: List[ProvinciaSchema] = []
        filas = await cls.__provincia.listar()
        for fila in filas:
            provincias.append(ProvinciaSchema(**fila[0].__dict__))
        return provincias

    @classmethod
    async def buscar_por_id(cls, id:int):
        return await cls.__provincia.obtener(id)
    
    @classmethod
    async def listar_cantones_por_provincia(cls,id_provincia:int):
        cantones: List[CantonSchema] = []
        filas = await cls.__canton.filtarPor(provincia_id= id_provincia)
        for fila in filas:
            cantones.append(CantonSchema(**fila[0].__dict__))
        return cantones

