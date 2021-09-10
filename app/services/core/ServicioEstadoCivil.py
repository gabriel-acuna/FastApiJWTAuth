from app.schemas.core.EtniaSchema import EtniaSchema
from typing import List
from app.schemas.core.EstadoCivilSachema import *
from app.models.core.modelos_principales import EstadoCivil


class ServicioEstadoCivil():

    @classmethod
    async def listar(cls) -> List[EstadoCivilSchema]:
        estados_civiles: List[EstadoCivilSchema] = []
        try:
            filas = await EstadoCivil.listar()
            for fila in filas:
                estados_civiles.append(
                    EstadoCivilPutSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        return estados_civiles

    @classmethod
    async def buscar_por_id(cls, id: int):
        try:
            return await EstadoCivil.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def agregar_registro(cls, estado_civil: EstadoCivilPostSchema):
        try:
            return await EstadoCivil.crear(
                estado_civil=estado_civil.estado_civil
            )
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
    
    @classmethod
    async def actualizar_registro(cls, estado_civil: EstadoCivilPutSchema):
        try:
            return await EstadoCivil.actualizar(id=estado_civil.id, estado_civil=estado_civil.estado_civil)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def eliminar_registro(cls, id: int):
        try:
            return await EstadoCivil.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def existe(cls, estado_civil: EstadoCivil) -> bool:
        try:
            existe = await EstadoCivil.filtarPor(estado_civil = estado_civil.estado_civil)
            if existe:
                return True
            return False
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
