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
        try:
            filas = await cls.__provincia.listar()
            for fila in filas:
                provincias.append(ProvinciaSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
        return provincias

    @classmethod
    async def buscar_por_id(cls, id: int):
        try:
            return await cls.__provincia.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")

    @classmethod
    async def listar_cantones_por_provincia(cls, id_provincia: int):
        cantones: List[CantonSchema] = []
        try:
            filas = await cls.__canton.filtarPor(provincia_id=id_provincia)
            for fila in filas:
                cantones.append(CantonSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
        return cantones
